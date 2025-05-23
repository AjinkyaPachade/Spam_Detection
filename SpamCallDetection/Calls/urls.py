from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.api_overview, name='api-overview'),
    path('api/check-number/<str:number>/', views.check_number, name='check-number'),
]
