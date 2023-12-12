from django.shortcuts import render

# Create your views here.
def noel(request):
    return render(request, "noel/index.html")