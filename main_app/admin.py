from django.contrib import admin
# import your models here
from .models import Seed, Watering

# Register your models here
admin.site.register(Seed)
admin.site.register(Watering)

