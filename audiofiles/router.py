from audiofilesapi.viewsets import songViewset, podecastViewset, audioBookViewset
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('song', songViewset)
routers.register('podecast', podecastViewset)
routers.register('audiobook', audioBookViewset)
