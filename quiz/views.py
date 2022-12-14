from django.shortcuts import render

def frontend(request):
    return render(request, "frontend.html")

def gameloading(request):
    return render(request, "gameloading.html")

def gameend(request):
    return render(request, "gameend.html")

def QandA(request):
    return render(request, "QandA.html")
    
def quiz2(request):
    return render(request, "quiz2.html")

def quiz3(request):
    return render(request, "quiz3.html")

def quiz4(request):
    return render(request, "quiz4.html")

def quiz5(request):
    return render(request, "quiz5.html")
    
