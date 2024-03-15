from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import *
from . serializer import *
# Create your views here.

# class ReactView(APIView):
    def get(self, request):
        output = []