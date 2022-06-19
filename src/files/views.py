from django.http import Http404
from django.shortcuts import render
from rest_framework import status, views
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from files.models import File
from files.serializers import FileSerializer

# Create your views here.
def get_object(self, pk):
  try:
    return File.objects.get(pk=pk)
  except File.DoesNotExist:
    raise Http404

# GET files?organizationId={org_id}
# GET files?userId={user_id}
@api_view(['GET'])
def file_list(request):
  files = File.objects.all()
  serializer  = FileSerializer(files, many=None)
  permission_classes = [IsAuthenticated] # TODO: Does this works?
  return Response(serializer.data)

# GET files/{file_id}
@api_view(['GET'])
def file_download(request, pk, format=None):
    file = get_object(pk)
    serializer = FileSerializer(file)
    return Response(serializer.data)

# POST files/upload 
@api_view(['POST'])
def file_upload(request, format=None):
  serializer = FileSerializer(data=request.data)
  
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)