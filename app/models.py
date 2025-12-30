from django.db import models

# Create your models here.
class SCHOOL(models.Model):
    name = models.CharField(max_length=100)
    year_of_establishment = models.IntegerField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='school_images/')
    

    def __str__(self):
        return self.name