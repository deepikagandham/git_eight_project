from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':13000,'b':1000,'c':1005}
    return render(request,'conditions.html',d)