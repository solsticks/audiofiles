from rest_framework import serializers
from .models import song, podcast, audioBook


class songSerializers(serializers.ModelSerializer):
    class Meta:
        model = song
        fields = '__all__'


class podcastSerializers(serializers.ModelSerializer):
    class Meta:
        model = podcast
        fields = '__all__'


class audioBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = audioBook
        fields = '__all__'
