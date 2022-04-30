from django.db import models

# Create your models here.
class Forme(models.Model):
    nom = models.CharField('Nom de la forme', max_length=20) #Bloc
    description = models.CharField('Description de la forme', max_length=200) #L'objet le plus commun du jeu de la vie. C'est la plus petite structure stable.
    cellules = models.TextField('Cellules qui composent la forme') #[[0,0],[0,1],[1,0],[1,1]]

    def __str__(self) -> str:
        return (str(self.nom,": ",self.desccription))