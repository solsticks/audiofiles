from rest_framework import serializers
from .models import song, podecast, audioBook


class songSerializers(serializers.ModelSerializer):
    class Meta:
        model = song
        fields = '__all__'


class podecastSerializers(serializers.ModelSerializer):
    class Meta:
        model = podecast
        fields = '__all__'


class audioBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = audioBook
        fields = '__all__'
