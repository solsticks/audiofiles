from audiofilesapi.viewsets import songViewset, podcastViewset, audioBookViewset
from rest_framework import routers


routers = routers.DefaultRouter()
routers.register(r'song', songViewset, basename='song')
routers.register('podcast', podcastViewset)
routers.register('audiobook', audioBookViewset)

