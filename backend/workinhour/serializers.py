from rest_framework import serializers
from .models import Person, CCTVFootage, CCTVCamera

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'email', 'photo']

class CCTVCameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCTVCamera
        fields = ['id', 'location', 'camera_id', 'description']

class CCTVFootageSerializer(serializers.ModelSerializer):
    camera = CCTVCameraSerializer(read_only=True)
    person = PersonSerializer(read_only=True)

    class Meta:
        model = CCTVFootage
        fields = ['id', 'person', 'timestamp', 'camera', 'image', 'is_entry']
