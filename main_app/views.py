from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Seed

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
  return render(request, 'seeds/detail.html', { 'seed': seed })

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