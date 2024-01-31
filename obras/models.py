from django.db import models

# Create your models here.
class Obra(models.Model):
    id_obra     = models.AutoField(db_column='id_obra', primary_key=True)
    artista     = models.CharField(max_length=20, blank= True, null=True)    
    nombre      = models.CharField(max_length=20, blank=True, null= True)
    material    = models.CharField(max_length=20, blank=True, null=True)
    tecnica     = models.CharField(max_length=20, blank=True, null=True)
    tamaño      = models.IntegerField(blank=True, null=True)
    precio      = models.IntegerField(blank=True, null=True)
    stock       = models.IntegerField(blank=True, null=True)
    pedido_choices   = [
        ('Si', 'Si'),
        ('No', 'No'),
    ]
    pedido           = models.CharField(max_length=5, choices=pedido_choices, blank=True, null=True)
    categoria_choices= [
        ('Digital', 'Digital'),
        ('Tradicional', 'Tradicional'),
        ('Escultura', 'Escultura'),
        ('Fotografia', 'Fotografia'),
    ]
    categoria        = models.CharField(max_length=20, choices= categoria_choices, blank=True, null=True)
    descripcion      = models.CharField(max_length=100, blank=True, null=True)

    imagen = models.ImageField(upload_to='obras_imagenes/', blank=True, null=True)

    def __str__(self):
        return str(self.nombre)+ " " +str(self.precio)+ " " +str(self.categoria)+ " "+ str(self.artista)
