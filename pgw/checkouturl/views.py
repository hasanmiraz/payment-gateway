from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from . import models

# Create your views here.

def debugTool(**kwargs):
    print("-"*30)
    for key, value in kwargs.items():
        print(f"task = {key}, taskResult = {value}\n")
    print("-"*30)

@api_view(["GET"])
def test(request):
    if request.method == "GET":
        data = {
            "name": "test"
        }
        return Response(data)