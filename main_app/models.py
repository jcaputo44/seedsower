from django.db import models
from django.urls import reverse

# Create your models here.
class Seed(models.Model):
    #first define the attributes/fields
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    #django will create inputs for a form and
    #text filed will create a <text area> not reugular <input>
    description = models.TextField(max_length=250)
    season = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'seed_id': self.id})