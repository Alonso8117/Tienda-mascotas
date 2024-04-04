from django.db import models

# Create your models here.


class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nom_categoria = models.CharField(max_length=100)


class Usuario(models.Model):
    rut = models.CharField(
        primary_key=True, verbose_name='Rut de la usuario', max_length=100)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=50)
    n_telefono = models.IntegerField()
    contra = models.CharField(max_length=30)


class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nom_producto = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()
    cantidad = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.CharField(max_length=250)

    def __str__(self):
        return self.nom_producto


class Venta(models.Model):
    n_venta = models.AutoField(primary_key=True)
    total_venta = models.IntegerField()
    descuento = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class DetalleVenta(models.Model):
    n_detalleventa = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total =  models.IntegerField()


class Carrito(models.Model):
    idCarrito = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=15)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario
