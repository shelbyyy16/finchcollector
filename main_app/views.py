from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch

# finches = [
#   {'name': 'Hoot', 'family': 'Owl Finch', 'description': 'curious and gregarious', 'age': 3},
#   {'name': 'Casa', 'family': 'House Finch', 'description': 'social butterfly', 'age': 2},
#   {'name': 'Queenie', 'family': 'Diamond Firetail', 'description': 'sassy and a touch aggressive', 'age': 2},
# ]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', { 'finch': finch })

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'

  def get_success_url(self):
    return reverse_lazy('detail', kwargs={'finch_id': self.object.id})

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['family', 'description', 'age']

  def get_success_url(self):
    return reverse_lazy('detail', kwargs={'finch_id': self.object.id})

class FinchDelete(DeleteView):
  model = Finch

  def get_success_url(self):
    return reverse_lazy('index')