from rest_framework import serializers
from .models import SimpleModel


class SimpleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleModel
        fields = ['id', 'name', 'description']
