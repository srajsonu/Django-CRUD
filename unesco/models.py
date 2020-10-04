from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class ISO(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    justification = models.TextField()
    year = models.IntegerField(null=True)
    longitude = models.DecimalField(null=True)
    latitude = models.DecimalField(null=True)
    area_hectares = models.DecimalField(max_digits=10,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    states = models.ForeignKey(State, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(ISO, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
