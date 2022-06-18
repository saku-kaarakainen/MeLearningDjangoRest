from rest_framework import serializers
from files.models import File


class FileSerializer(serializers.Serializer):
  class Meta:
    model = File
    files= ('name')
