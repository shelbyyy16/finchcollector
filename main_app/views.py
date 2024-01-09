from django.shortcuts import render

finches = [
  {'name': 'Hoot', 'family': 'Owl Finch', 'description': 'curious and gregarious', 'age': 3},
  {'name': 'Casa', 'family': 'House Finch', 'description': 'social butterfly', 'age': 2},
  {'name': 'Queenie', 'family': 'Diamond Firetail', 'description': 'sassy and a touch aggressive', 'age': 2},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })
