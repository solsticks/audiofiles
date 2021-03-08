import json

from django.test import TestCase
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIRequestFactory

from audiofilesapi.models import song, audioBook, podecast
from audiofilesapi.serializer import songSerializers
from audiofilesapi.viewsets import songViewset, audioBookViewset, podecastViewset


class createSong(APITestCase):

    def test_song(self):
        data = json.dumps({"Name": "rainy day", "Duration": 60, "uploadTime": "2021-08-12T00:00"})
        response = self.client.post('/api/song/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class getSong_test(APITestCase):

    def test_view_set(self):
        request = APIRequestFactory().get("")
        song_details = songViewset.as_view({'get': 'retrieve'})
        employee = song.objects.create(Name="snowy", Duration=120, uploadTime="2021-08-12")
        response = song_details(request, pk=employee.pk)
        self.assertEqual(response.status_code, 200)


