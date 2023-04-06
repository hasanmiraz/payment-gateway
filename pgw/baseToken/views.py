from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TokeenSerializer

import secrets

# Create your views here.

@api_view(["GET"])
def grantToken(request):
    data = {"sec" : secrets.token_urlsafe(512)}
    return Response(data)
