from django.urls import path
from .views import *

urlpatterns = [
    path('fizzbuzz', FizzBuzzView.as_view(), name='fizzbuzz' ),
    
]

