from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Module(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.titre


class Inscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Cours(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    contenu = models.TextField()

    def __str__(self):
        return self.titre
