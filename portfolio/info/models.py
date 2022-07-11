from django.db import models

# Create your models here.
class Quote(models.Model):
    quote=models.TextField()

    def __str__(self) -> str:
        return self.quote

class About(models.Model):
    descTitle=models.TextField()
    description = models.TextField()
    image= models.ImageField()
    cv= models.URLField()

    def __str__(self) -> str:
        return self.descTitle

class Work(models.Model):
    title=models.CharField(max_length=50)
    description = models.TextField()
    image=models.ImageField(blank=True, null =True)
    role=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title

class Testimonies(models.Model):
    name= models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    workplace = models.CharField(max_length=10)
    worksite = models.URLField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Technologies(models.Model):
    techName = models.CharField(max_length=20)
    techImage = models.ImageField()

    def __str__(self) -> str:
        return self.techName


