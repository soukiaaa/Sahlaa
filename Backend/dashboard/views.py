from django.shortcuts import render

# Create your views here.
# dashboard/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'ecom-dashboard/index.html')
