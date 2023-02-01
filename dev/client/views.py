import math

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client
from .serializers import ClientSerializer

# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class TopRiskClients(APIView):

    def get(self, request, format=None):
        clients_score = {}
        clients = Client.objects.all()
        for client in clients:
            sd = 0
            data = ClientSerializer(client).data
            name = data['name']
            health_problems = data['health_problem']
            for health_problem in health_problems:
                sd += health_problem['grade']
            
            score = (1 / (1+ math.exp(-(-2.8 + sd)))) * 100
            clients_score[name] = score

        clients_score = sorted(clients_score.items(), key=lambda x:x[1], reverse=True)
        clients_score = dict(clients_score)
        return Response(clients_score)
