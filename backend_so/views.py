from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics,permissions
from rest_framework.authtoken.models import Token 
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from django.db import IntegrityError
from rest_framework import serializers 
from .models import Producto, Cliente, Venta, DetalleVenta
from .serializers import (
    LoginSerializer,
    ProductoSerializer,
    ClienteSerializer,
    VentaSerializer,
    DetalleVentaSerializer,
    RegisterSerializer
)

# Vista para el inicio de sesión
class LoginView(APIView):
    permission_classes = [AllowAny]  # Permitir acceso a todos

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data  # Este es el usuario autenticado

        # Obtener o crear un token para el usuario
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'message': 'Login successful',
            'user': {
                'email': user.email,
                'id': user.id,
            },
            'token': token.key  # Retorna el token en la respuesta
        }, status=status.HTTP_200_OK)

 # Importa AllowAny

class RegisterClientView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            user = serializer.save()  # Crea el usuario
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'message': 'User registered successfully',
                'user': {
                    'id': user.id,
                    'email': user.email,
                },
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        
        except IntegrityError:
            return Response({'detail': 'Email already registered.'}, status=status.HTTP_400_BAD_REQUEST)

# Clases de vista para los modelos
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [AllowAny]  # Permitir acceso público

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    authentication_classes = [TokenAuthentication]  # Requerir token
    permission_classes = [IsAuthenticated]  # Requerir que el usuario esté autenticado
    def perform_create(self, serializer):
        serializer.save()  # Solo guarda el serializer; el cliente se maneja dentro del serializer

class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer
    permission_classes = [permissions.IsAuthenticated]

class ListaComprasView(generics.ListAPIView):
    serializer_class = VentaSerializer
    def get_queryset(self):
        # Filtrar las ventas del cliente asociado al usuario autenticado
        return Venta.objects.filter(cliente__user=self.request.user)