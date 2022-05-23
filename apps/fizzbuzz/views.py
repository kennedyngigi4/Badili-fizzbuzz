from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.



class FizzBuzzView(generics.ListCreateAPIView):
    serializer_class = FizzBuzzSerializer
    queryset = Fizzbuzz.objects.all()

    def post(self, request, *args, **kwargs):
        input = int(request.data['num_input'])

        if input % 5 == 0 and input % 7 ==0:
            return Response({"For both: ": "LR"})
        elif input % 5 == 0:
            return Response({"For 5: ": "L"})
        elif input % 7 == 0:
            return Response({"For 7: ": "R"})
        
        return Response({"None: ": input})



