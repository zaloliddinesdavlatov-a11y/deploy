from django.shortcuts import render
from rest_framework import generics
from .models import BookModel
from .serializers import BookSerializers

class BookListApiView(generics.ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers


class BookCreateApiView(generics.CreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers


class BookEditApiView(generics.UpdateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers
    lookup_field = 'pk'


class BookDeleteApiView(generics.DestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers


class BookDetailApView(generics.RetrieveAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers


class BookMixedApView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers

