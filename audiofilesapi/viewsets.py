from rest_framework import viewsets
from . import models
from . import serializer


class songViewset(viewsets.ModelViewSet):
    queryset = models.song.objects.all()
    serializer_class = serializer.songSerializers


class podecastViewset(viewsets.ModelViewSet):
    queryset = models.podecast.objects.all()
    serializer_class = serializer.podecastSerializers


class audioBookViewset(viewsets.ModelViewSet):
    queryset = models.audioBook.objects.all()
    serializer_class = serializer.audioBookSerializers
