from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio = models.IntegerField()
    def __str__(self):
        return f'{self.nombre} -> {self.precio}'

class Carrito(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    isOpen = models.BooleanField(default = True)

class CarritoProductos(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.IntegerField()
    id_carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)

class PurchasedProducts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total = models.FloatField()

 #nombre = models.CharField(max_length=50)
  #  apellido = models.CharField(max_length=100)
   # correo = models.EmailField(max_length=100)
    #password = models.CharField(max_length=50, default='')
    #telefono = models.PositiveBigIntegerField()
    #direccion = models.CharField(max_length=200)