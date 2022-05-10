from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Seed
from .forms import WateringForm


# Create your views here.


# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def seeds_index(request):
  seeds = Seed.objects.all()
  return render(request, 'seeds/index.html', { 'seeds': seeds })

def seeds_detail(request, seed_id):
  seed = Seed.objects.get(id=seed_id)
  watering_form = WateringForm()
  return render(request, 'seeds/detail.html', { 
    'seed': seed, 
    'watering_form': watering_form
    })
  
def add_watering(request, seed_id):
  # create a ModelForm instance using the data in request.POST
  form = WateringForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the seed_id assigned
    new_watering = form.save(commit=False)
    new_watering.seed_id = seed_id
    new_watering.save()
  return redirect('detail', seed_id=seed_id)

class SeedCreate(CreateView):
  model = Seed
  fields = '__all__'

class SeedUpdate(UpdateView):
  model = Seed
  # Let's disallow the renaming of a Seed by excluding the name field!
  fields = ['type', 'description', 'season']

class SeedDelete(DeleteView):
  model = Seed
  success_url = '/seeds/'