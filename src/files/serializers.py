from rest_framework import serializers
from files.models import File


class FileSerializer(serializers.Serializer):
  
  def create(self, data):
    return File(**data)
  
  class Meta:
    model = File
    fields = ['name']
