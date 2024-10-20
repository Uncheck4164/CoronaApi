from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Corona
from .serializers import CoronaSerializer
from django.shortcuts import render
import os
import json

# Create your views here.

@api_view(['GET'])
def get_products_data(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, 'productos_limpios.json')
    
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    return JsonResponse(data, safe=False)



    
