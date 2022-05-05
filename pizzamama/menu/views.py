from django.shortcuts import render
from .models import Pizza
from django.http import HttpResponse
# Create your views here.
def index(request):
    pizzas=Pizza.objects.all().order_by('prix')
    return render(request,'menu/index.html',{'pizzas':pizzas})
    #recupération de la collection d'ojets
    """ 
    pizzas_names_and_prices=[pizza.nom + " : " +str(pizza.prix) + "£" for pizza in pizzas]
    pizzas_names_and_prices_str=", ".join(pizzas_names_and_prices)
    return HttpResponse("Les pizzas : " + pizzas_names_and_prices_str)"""
   