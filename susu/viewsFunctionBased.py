# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Client
from rest_framework import viewsets
from .serializers import ClientSerializer
#
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from susu.models import Client


@api_view(['GET', 'POST'])
def client_list(request, format=None):
    """
       List all clients, or create a new client.
    """
    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, pk, format=None):
    """
        Retrieve, update or delete a client instance.
    """
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class ClientAllViewSet(viewsets.ModelViewSet):
#     """
#      API endpoint that allows Clients to be viewed or edited.
#     """
#     queryset = Client.objects.all().order_by('lastName')
#     serializer_class = ClientSerializer

