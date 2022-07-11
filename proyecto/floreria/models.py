from django.db import models

# Create your models here.

#modelo para Categoria
class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=30, verbose_name='Nombre Categoria')
    

    def __str__(self):
        return self.nombreCategoria



class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=20, verbose_name="Nombre Producto:")
    precio = models.IntegerField(verbose_name="Precio Producto:")
    imagen = models.ImageField(upload_to= 'imagenes/',null=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nombre_producto

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
    