from django.db import models

# Create your models here.


class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telephone = models.CharField(max_length=100)
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=100)

    def __str__(self):
        return self.nom + ' ' + self.prenom
