from django.db import models

# Create your models here.
#Contains ce que on veut mémoriser dans la base de données
class Pizza(models.Model):
    nom = models.CharField(max_length=200)
    ingredients=models.CharField(max_length=400)
    prix=models.FloatField(default=0)
    vegetarienne=models.BooleanField(default=False)

    #afficher par défaut le nom
    def __str__(self):
        return self.nom
