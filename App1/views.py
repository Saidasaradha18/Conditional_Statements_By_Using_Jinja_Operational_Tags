from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':1000,'b':200,'c':300}
    return render(request,'conditions.html',d)