from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Producto, Cliente, Venta, DetalleVenta

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)  # Solo escritura para mayor seguridad

    def validate(self, attrs):
        # Autenticar el usuario usando el email como username
        user = authenticate(username=attrs['email'], password=attrs['password'])
        if user is None:
            raise serializers.ValidationError('Invalid email or password')  # Mensaje de error más claro
        return user
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])  # Encriptar contraseña
        user.save()
        return user

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    telefono = serializers.CharField(required=False)  # Si deseas permitir un número de teléfono opcional
    direccion = serializers.CharField(required=False)  # Si deseas permitir una dirección opcional

    class Meta:
        model = User
        fields = ['email', 'password', 'telefono', 'direccion']  # Agregar los campos opcionales aquí

    def create(self, validated_data):
        # Extraer el teléfono y la dirección si están presentes
        telefono = validated_data.pop('telefono', None)
        direccion = validated_data.pop('direccion', None)

        # Crear el usuario
        user = User(
            email=validated_data['email'],
            username=validated_data['email'],  # Usa el email como username
        )
        user.set_password(validated_data['password'])
        user.save()

        # Crear el cliente asociado al usuario
        cliente = Cliente.objects.create(
            user=user,
            telefono=telefono,
            direccion=direccion,
        )

        return user

        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('user', 'telefono', 'direccion')  


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'




class DetalleVentaSerializer(serializers.ModelSerializer):
    producto_id = serializers.IntegerField()
    producto = ProductoSerializer(read_only=True)   # Este campo permanece para recibir el ID del producto.

    class Meta:
        model = DetalleVenta
        fields = ['producto_id', 'cantidad','producto'] 

class VentaSerializer(serializers.ModelSerializer):
    detalles = DetalleVentaSerializer(many=True)  # Se mantiene como un campo anidado

    class Meta:
        model = Venta
        fields = ['id','fecha','detalles', 'total']

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles')  # Extraer detalles de la venta
        user = self.context['request'].user  # Obtener el usuario autenticado

        if user.is_anonymous:
            raise serializers.ValidationError("Usuario no autenticado.")

        # Obtener el cliente asociado al usuario autenticado
        try:
            cliente = Cliente.objects.get(user=user)
        except Cliente.DoesNotExist:
            raise serializers.ValidationError("Cliente no encontrado para este usuario.")

        # Crear la venta asociando el cliente
        venta = Venta.objects.create(cliente=cliente, total=validated_data['total'])

        # Crear los detalles de la venta
        for detalle_data in detalles_data:
            # Extraer el producto_id
            producto_id = detalle_data.get('producto_id')  # Usamos get para evitar KeyError
            cantidad = detalle_data.get('cantidad')

            if producto_id is None:
                raise serializers.ValidationError("El campo 'producto_id' es requerido en los detalles.")
            if cantidad is None:
                raise serializers.ValidationError("El campo 'cantidad' es requerido en los detalles.")

            # Buscar el producto
            try:
                producto = Producto.objects.get(id=producto_id)  # Usar el id del producto
            except Producto.DoesNotExist:
                raise serializers.ValidationError(f"Producto con ID {producto_id} no encontrado.")

            # Verificar si hay suficiente stock
            if producto.cantidad_en_stock < cantidad:
                raise serializers.ValidationError(f"No hay suficiente stock para el producto '{producto.nombre}'.")

            # Crear el detalle de la venta
            DetalleVenta.objects.create(
                venta=venta,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=producto.precio
            )

            # Actualizar la cantidad en stock
            producto.cantidad_en_stock -= cantidad
            producto.save()

        return venta



