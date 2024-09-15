from django.contrib import admin
from .models import (
    Producto,
    Cliente,
    Venta,
    DetalleVenta,
    Proveedor,
    OrdenCompra,
    DetalleOrdenCompra,
    Cuenta,
    Administrador
)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad_en_stock')
    search_fields = ('nombre',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
    search_fields = ('nombre', 'email')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha_venta', 'total')
    list_filter = ('fecha_venta',)

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('venta', 'producto', 'cantidad', 'precio_unitario')

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contacto', 'telefono')
    search_fields = ('nombre',)

@admin.register(OrdenCompra)
class OrdenCompraAdmin(admin.ModelAdmin):
    list_display = ('proveedor', 'fecha_orden', 'estado')
    list_filter = ('fecha_orden', 'estado')

@admin.register(DetalleOrdenCompra)
class DetalleOrdenCompraAdmin(admin.ModelAdmin):
    list_display = ('orden_compra', 'producto', 'cantidad', 'precio_unitario')

@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('email', 'rol', 'activo')

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cuenta', 'telefono')
    search_fields = ('nombre', 'cuenta__email')
