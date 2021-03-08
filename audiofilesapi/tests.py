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


# class getEmployee_test(APITestCase):
# def test_view_set(self):
# request = APIRequestFactory().put("")
# employee_details = employeesViewset.as_view({'put': 'update'})
# employee = employees.objects.create(empId=9, firstName="james", lastName="thom")
# response = employee_details(request, pk=employee.pk)
# self.assertEqual(response.status_code, 200)

class UpdateSingleSongTest(APITestCase):
    """ Test module for updating an existing song record """

    def setUp(self):
        self.goodCode = song.objects.create(
            Name='goodCode', Duration='90', uploadTime='2021-08-12T00:00')
        self.greatCOde = song.objects.create(
            Name='greatCode', Duration=130, uploadTime='2021-06-12T00:00')
        self.valid_payload = {
            'Name': 'goodCode',
            'Duration': 120,
            'uploadTime': '2021-08-12T00:00',
        }
        self.invalid_payload = {
            'Name': '',
            'Duration': 110,
            'uploadTime': '2021-06-12T00:00',
        }

    def test_valid_update_song(self):
        response = self.client.put('/api/song/', kwargs={'pk': self.greatCOde.pk}, data=json.dumps(self.valid_payload),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_song(self):
        response = self.client.put('/api/song/', kwargs={'pk': self.greatCOde.pk},
                                   data=json.dumps(self.invalid_payload),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'DELETE', 'PUT'])
    def get_delete_update_song(self, pk):
        try:
            Song = song.objects.get(pk=pk)
        except song.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # get details of a single song
        if self.method == 'GET':
            serializer = songSerializers(Song)
            return Response(serializer.data)

        # update details of a single song
        if self.method == 'PUT':
            serializer = songSerializers(Song, data=self.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # delete a single song
        elif self.method == 'DELETE':
            return Response({})
