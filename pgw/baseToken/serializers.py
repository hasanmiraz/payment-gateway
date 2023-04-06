from rest_framework import serializers
from .models import Tokens

class TokeenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tokens
        fields = '__all__'