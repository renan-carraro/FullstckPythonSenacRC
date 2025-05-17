from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')
def sobre(request):
    return render(request,'sobre.html')
def curso(request):
    return render(request,'curso.html')