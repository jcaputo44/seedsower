from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class Seed:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, type, description, season):
    self.name = name
    self.type = type
    self.description = description
    self.season = season

seeds = [
  Seed('Carrot', 'root vegetable', 'sweet and crucnhy', 'spring'),
  Seed('Beet', 'root vegetable', 'colorful, dynamic, easy to grow', 'fall and spring'),
  Seed('Broccoli', 'cruciferous vegetable', 'slow growing but good for the soul', 'spring')
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Sow Dem Seeds</h1>')

def about(request):
  return render(request, 'about.html')

def seeds_index(request):
  return render(request, 'seeds/index.html', { 'seeds': seeds })