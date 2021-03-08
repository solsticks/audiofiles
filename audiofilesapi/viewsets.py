from rest_framework import viewsets
from . import models
from . import serializer


class songViewset(viewsets.ModelViewSet):
    queryset = models.song.objects.all()
    serializer_class = serializer.songSerializers


class podcastViewset(viewsets.ModelViewSet):
    queryset = models.podcast.objects.all()
    serializer_class = serializer.podcastSerializers


class audioBookViewset(viewsets.ModelViewSet):
    queryset = models.audioBook.objects.all()
    serializer_class = serializer.audioBookSerializers
