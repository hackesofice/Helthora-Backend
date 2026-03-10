from rest_framework import serializers
from . import models

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = "__all__"

class doctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctors
        fields = "__all__"