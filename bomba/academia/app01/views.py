from django.shortcuts import render
from .models import Produtos

def home(request):
    return render(request,'home.html')
def contatos(request):
    return render(request,'contatos.html')
def produtos(request):
    produtos = Produtos.objects.all()
    return render(request, 'app01/produtos.html', {'produtos': produtos})