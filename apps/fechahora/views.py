from django.http import request
from django.http.request import HttpRequest
from django.shortcuts import render, HttpResponse
# from time import gmtime, strftime
from datetime import datetime

# Create your views here.
# def index(request):
#     context = {
#         "time": strftime("%d-%m-%Y %H:%M %p", gmtime())
#     }
#     return render(request, "index.html", context)

def index(request):
    now = datetime.now()
    
    context = {
        "fecha": now.strftime('Día :%d, Mes :%m, Año :%Y'),
        "tiempo": now.strftime('Hora  %H : %M minutos %S seg.')
    }
    return render(request, "index.html", context)