from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductoViewSet,
    ClienteViewSet,
    VentaViewSet,
    DetalleVentaViewSet,
    LoginView,
    RegisterClientView,
    ListaComprasView
)

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'detalleventas', DetalleVentaViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login/', LoginView.as_view(), name='login'),  # Ruta de login
    path('api/register/', RegisterClientView.as_view(), name='register'),  # Ruta de registro
    path('compras/', ListaComprasView.as_view(), name='lista_compras'),
]
