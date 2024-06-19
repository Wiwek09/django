from rest_framework import serializers
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        modal = User
        fields = ['id','first_name','last_name',  'email','password']

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()