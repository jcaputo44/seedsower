from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Seed, Plot
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
  id_list = seed.plots.all().values_list('id')
  plots_not_planted = Plot.objects.exclude(id__in=id_list)
  watering_form = WateringForm()
  return render(request, 'seeds/detail.html', { 
    'seed': seed, 
    'watering_form': watering_form,
    'plots': plots_not_planted
    })

def assoc_plot(request, seed_id, plot_id):
  # Note that you can pass a plot's id instead of the whole plot object
  Seed.objects.get(id=seed_id).plots.add(plot_id)
  return redirect('detail', seed_id=seed_id)

def unassoc_plot(request, seed_id, plot_id):
  # Note that you can pass a plot's id instead of the whole plot object
  Seed.objects.get(id=seed_id).plots.remove(plot_id)
  return redirect('detail', seed_id=seed_id)
  
class SeedCreate(CreateView):
  model = Seed
  fields = ['type', 'description', 'season', 'date_planted']

class SeedUpdate(UpdateView):
  model = Seed
  # Let's disallow the renaming of a Seed by excluding the name field!
  fields = ['type', 'description', 'season', 'date_planted']

class SeedDelete(DeleteView):
  model = Seed
  success_url = '/seeds/'

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

class PlotList(ListView):
  model = Plot
  # fields = ['name', 'zone']

class PlotDetail(DetailView):
  model = Plot
  fields = ['name', 'zone']

class PlotCreate(CreateView):
  model = Plot
  fields = ['name', 'zone']

class PlotUpdate(UpdateView):
  model = Plot
  fields = ['name', 'zone']

class PlotDelete(DeleteView):
  model = Plot
  success_url = '/plots/'