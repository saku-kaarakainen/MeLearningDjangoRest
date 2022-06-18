from django.http import Http404
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from models import ApiUser, File
from serializers import FileSerializer

# Create your views here.

class FileList(generics.ListAPIView):
  queryset = File.objects.All()
  serializer_class = FileSerializer
  permission_classes = [IsAuthenticated]

class FileDownload(generics.RetrieveAPIView):
  serializer_class = FileSerializer
  queryset = File.objects.first()
  permission_classes = [IsAuthenticated]

# TODO: How do I define the correct HTTP verb?
class FileUpload(generics.CreateAPIView):
  # source to be used so far: https://github.com/juanbenitezdev/django-rest-framework-crud/blob/master/movies/views.py
  raise NotImplemented('TODO')