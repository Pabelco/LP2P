# from django.shortcuts import render
# from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import Basurero
from .models import Usuario
from .models import BasureroCalificado
# Create your views here.
trashes = [
    {'name':'fiec','latitude':'-2.144753','longitude':'-79.966804'},
    {'name':'fsch','latitude':'-19.2','longitude':'-434.2'}
]

def get_trashes(request):
    trashes = serializers.serialize('json', Basurero.objects.all())
    data = {
        'trashes': trashes
    }
    return JsonResponse(data)


    #Cosas de Prueba
    # data = {
    #     'trashes': Basurero.objects.all()
    # }
    # return render(request,'trash.html',data)
    # return HttpResponse('<h1>LocateTrash</h1>')


