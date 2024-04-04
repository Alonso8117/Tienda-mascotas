from typing_extensions import Required
from django.shortcuts import redirect, render
from .models import DetalleVenta, Producto, Carrito, Usuario, Venta
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.


def index(request):
    productos = Producto.objects.all()  # convierte la tabla en un objeto
    contexto = {"producto": productos}
    return render(request, 'core/index.html', contexto)


def correas(request):
    # select * from productos where categoria_id = 2
    productos = Producto.objects.filter(categoria_id=2)
    contexto = {"producto": productos}
    return render(request, 'core/correas.html', contexto)


def identificador(request):
    # select * from productos where categoria_id = 3
    productos = Producto.objects.filter(categoria_id=3)
    contexto = {"producto": productos}
    return render(request, 'core/identificador.html', contexto)


def historial(request):
    return render(request, 'core/historial.html')


def carro(request):
    # select * from productos where categoria_id = 3
    carritos = Carrito.objects.filter(usuario='123456789')
    contexto = {"carrito": carritos}
    return render(request, 'core/carro.html', contexto)


def bandana(request):
    # select * from productos where categoria_id = 1
    productos = Producto.objects.filter(categoria_id=1)
    contexto = {"producto": productos}
    return render(request, 'core/bandanas.html', contexto)


def inicio(request):
    return render(request, 'core/inicio.html')


def register(request):
    return render(request, 'core/register.html')


def iniciar_sesion(request):
    return render(request, 'core/iniciar_sesion.html')


def agregar_carrito(request, id):
    carrito = Carrito(usuario='123456789', producto_id=id)
    carrito.save()
    return redirect('carro')


def eliminar_producto_carrito(request, id):
    carrito = Carrito.objects.filter(
        producto_id=id).filter(usuario='123456789')
    carrito.delete()
    return redirect('carro')


def aut_user(request):
    email = request.POST['correo']
    Usuario.objects.filter(correo=email)
    return redirect('index')


def crear_usuario(request):
    nombre = request.POST['nombre']
    rut = request.POST['rut']
    telefono = request.POST['telefono']
    email = request.POST['correo']
    clave = request.POST['clave']
    user = Usuario(rut=rut, nombre=nombre, n_telefono=telefono,
                   correo=email, contra=clave)
    user.save()
    return redirect('iniciar_sesion')


def guardar_venta(request):
    carritos = Carrito.objects.filter(usuario='123456789')
    total = 0
    productos = []
    for c in carritos:
        total = total + c.producto.precio
        print(c.producto.id_producto)
        productos.append(c.producto.id_producto)
        detalleVenta = DetalleVenta(
            usuario_id='123456789', producto_id=c.producto.id_producto, cantidad=1, total=c.producto.precio)
        detalleVenta.save()
    venta = Venta(total_venta=total, descuento=0, usuario_id='123456789')
    venta.save()
    carrito = Carrito.objects.filter(usuario='123456789')
    carrito.delete()
    return redirect('index')
