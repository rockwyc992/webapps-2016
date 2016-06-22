from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import list_route
from .models import Shortener
from .serializers import Shortener_Serializer

class Shortener_ViewSet(viewsets.ModelViewSet):
    queryset = Shortener.objects.all()
    serializer_class = Shortener_Serializer

def Redirect(request, token):
    shortener = get_object_or_404(Shortener, short_url=token)
    shortener.click += 1
    shortener.save()
    return HttpResponseRedirect(shortener.long_url)

def Token_not_Found(request):
    return HttpResponse('hello')

def Index(request):
    return render(request, 'index.html', {})

def File(request, type, path):
    return render(request, type + '/' + path, {})

def handler404(request):
    return HttpResponseRedirect('http://seal.tw') 

