from django.shortcuts import render

def frontend(request):
    return render(request, "frontend.html")

def gameloading(request):
    return render(request, "gameloading.html")

def gameend(request):
    return render(request, "gameend.html")
    
    
