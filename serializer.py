from rest_framework import serializers
from . models import *

class ReactSerializer(serializer.ModelSerializer):
    class Mate:
        model = React
        fields = ['employee', 'department']