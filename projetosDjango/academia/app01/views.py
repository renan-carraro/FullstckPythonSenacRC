from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def produtos(request):
    return render (request,'produtos.html')
def contatos(request):
    return render(request,'contatos.html')