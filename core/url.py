from django.urls import path
from .views import bandana, carro,  historial, identificador, index, correas, agregar_carrito, eliminar_producto_carrito, inicio, register, iniciar_sesion, aut_user, crear_usuario, guardar_venta
urlpatterns = [
    path('', inicio, name="inicio"),
    path('inicio', index, name='index'),
    path('correas', correas, name="correas"),
    path('identificador', identificador, name="identificador"),
    path('historial', historial, name="historial"),
    path('carro', carro, name="carro"),
    path('bandana', bandana, name="bandana"),
    path('register', register, name="register"),
    path('iniciar_sesion', iniciar_sesion, name="iniciar_sesion"),
    path('carro/<id>', agregar_carrito, name="agregar_carrito"),
    path('delete/<id>', eliminar_producto_carrito,
         name="eliminar_producto_carrito"),
    path('aut_user', aut_user, name="aut_user"),
    path('crear_usuario', crear_usuario, name="crear_usuario"),
    path('guardar_venta', guardar_venta, name="guardar_venta"),

]
