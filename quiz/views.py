from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def gameloading(request):
    return render(request,'gameloading.html')
def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')
    
    
