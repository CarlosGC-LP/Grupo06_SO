from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  
from django.contrib.auth.models import User  
from .models import (
    Producto,
    Cliente,
    Venta,
    DetalleVenta
)


class CustomUserAdmin(UserAdmin):
    # Mostramos estos campos en la lista de usuarios
    list_display = ('email', 'first_name', 'last_name', 'is_staff')

    # Los campos que vamos a permitir editar al crear o modificar usuarios
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    # Campos a mostrar en el formulario de creación de usuarios
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )

# Registramos el modelo User con la configuración personalizada
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad_en_stock')
    search_fields = ('nombre',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'telefono', 'direccion')  # Cambiar 'nombre' y 'email' por 'user_email'

    def user_email(self, obj):
        return obj.user.email if obj.user else 'default@gmail.com'  # Manejar el caso de None
    user_email.short_description = 'Email'
    
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha', 'total')  # Cambia 'fecha_venta' a 'fecha'
    list_filter = ('fecha',)  # Cambia 'fecha_venta' a 'fecha'

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('venta', 'producto', 'cantidad', 'precio_unitario')

