from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse

from .models import List

def index(request):
    return render(request, 'index.html', {})

def ph(request, pk):
    list = List.objects.filter(homework=pk).order_by('problem')
    data = {};
    i = 0;
    for element in list:
        data[i] = element.problem
        i += 1

    return JsonResponse(data)
