import json

import pytz
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIRequestFactory

from audiofilesapi.models import song
from audiofilesapi.viewsets import songViewset

utc = pytz.UTC


class createSong(APITestCase):

    def test_song(self):
        data = json.dumps({"Name": "rainy day", "Duration": 60, "uploadTime": "2021-08-12T00:00"})
        response = self.client.post('/api/song/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class getSong_test(APITestCase):

    def test_view_set(self):
        request = APIRequestFactory().get("")
        song_details = songViewset.as_view({'get': 'retrieve'})
        songFile = song.objects.create(Name="snowy", Duration=120, uploadTime="2021-08-12")
        response = song_details(request, pk=songFile.pk)
        self.assertEqual(response.status_code, 200)


class UpdateSingleSongTest(APITestCase):
    """ Test module for updating an existing song record """

    def setUp(self):
        self.goodCode = song.objects.create(Name="goodCode", Duration="90", uploadTime="2021-08-12T00:00")

        self.greatCOde = song.objects.create(Name='greatCode', Duration=130, uploadTime='2021-06-12T00:00')

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
        edit_url = reverse('song-detail', args=[self.goodCode.pk])
        response = self.client.patch(edit_url, data=json.dumps(self.valid_payload),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)


class DeleteSinglsongTest(APITestCase):
    """ Test module for deleting an existing song record """

    def setUp(self):
        self.goodCode = song.objects.create(Name="goodCode", Duration="90", uploadTime="2021-08-12T00:00")

        self.greatCOde = song.objects.create(Name='greatCode', Duration=130, uploadTime='2021-06-12T00:00')

    def test_valid_delete_song(self):
        edit_url = reverse('song-detail', args=[self.goodCode.pk])
        response = self.client.delete(edit_url, kwargs={'pk': self.goodCode.pk})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_song(self):
        edit_url = reverse('song-detail', kwargs={'pk': 30})
        response = self.client.delete(edit_url, kwargs={'pk': 30})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


""" Test for the audioBook endpoints """
