from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response


class CalendarApi(APIView):

    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as function (get, post,put, patch, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application log'
        ]
        
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})        


def index(request):
    return HttpResponse('Hello')
    
    
# class date_assignments():