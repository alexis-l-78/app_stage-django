from django.db import models

class ACTEURS(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom



class FILMS(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
