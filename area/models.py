from django.db import models
from account.models import User

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Division(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)
    division = models.ForeignKey(Division, on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

class Area(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,)
    division = models.ForeignKey(Division, on_delete=models.CASCADE,)
    district = models.ForeignKey(District, on_delete=models.CASCADE,)

    def __str__(self):
        return self.user.username 