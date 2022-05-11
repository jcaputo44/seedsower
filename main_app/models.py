from django.db import models
from django.urls import reverse
from datetime import date
from django.utils.timezone import now

WATERED = (
    ('Y', 'YES'),
    ('N', 'NO')
)

class Plot(models.Model):
    name = models.CharField(max_length=50)
    zone = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plots_detail', kwargs={'pk': self.id})
        # Plots have a M:M related manager named seed_set

# Create your models here.
class Seed(models.Model):
    #first define the attributes/fields
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    #django will create inputs for a form and
    #text filed will create a <text area> not reugular <input>
    description = models.TextField(max_length=250)
    season = models.CharField(max_length=100)
    date_planted = models.DateField('Date Planted', default=now)
    # add a M:M association between seeds and plots
    plots = models.ManyToManyField(Plot)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'seed_id': self.id})

class Watering(models.Model):
    date = models.DateField()
    water = models.CharField('Watered?',
         max_length=1,
            choices=WATERED,
            default=WATERED[0][0]
         )

    seed = models.ForeignKey(Seed, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_water_display()} on {self.date}"

    class Meta:
        ordering = ['-date']