from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import PhoneNumber
from .serializers import PhoneNumberSerializer
# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def check_number_html(request):
    return render(request, 'check_number.html')

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Check Number': '/api/check-number/<str:number>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def check_number(request, number):
    phone_number = get_object_or_404(PhoneNumber, number=number)
    serializer = PhoneNumberSerializer(phone_number)
    return Response(serializer.data)
