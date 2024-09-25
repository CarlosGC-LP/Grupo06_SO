from django.db import models
from django.contrib.auth.models import User
class Producto(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_en_stock = models.IntegerField()
    urlImgProducto = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Hacer el campo nullable
    telefono = models.TextField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.email if self.user else 'defautl@gmail.com'

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha de creación de la venta

    def __str__(self):
        return f'Venta {self.id} - Cliente: {self.cliente}'

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Detalle de {self.venta} - Producto: {self.producto}'



