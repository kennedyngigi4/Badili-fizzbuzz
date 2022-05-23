from rest_framework import serializers
from .models import *

class FizzBuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fizzbuzz
        fields = '__all__'






