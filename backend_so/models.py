from django.db import models

class Producto(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_en_stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.TextField()
    email = models.EmailField(unique=True)
    telefono = models.TextField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Venta {self.id} - Cliente: {self.cliente.nombre}'

class DetalleVenta(models.Model):
    venta = models.ForeignKey('Venta', on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre} en Venta {self.venta.id}'

class Proveedor(models.Model):
    nombre = models.TextField()
    contacto = models.TextField(blank=True, null=True)
    telefono = models.TextField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class OrdenCompra(models.Model):
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    fecha_orden = models.DateTimeField(auto_now_add=True)
    estado = models.TextField()

    def __str__(self):
        return f'Orden {self.id} - Proveedor: {self.proveedor.nombre}'

class DetalleOrdenCompra(models.Model):
    orden_compra = models.ForeignKey('OrdenCompra', on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre} en Orden {self.orden_compra.id}'

class Cuenta(models.Model):
    email = models.EmailField(unique=True)
    password_hash = models.TextField()
    rol = models.TextField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.email

class Administrador(models.Model):
    cuenta = models.ForeignKey('Cuenta', on_delete=models.CASCADE)
    nombre = models.TextField()
    telefono = models.TextField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
