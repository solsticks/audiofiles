import datetime
import json

import pytz
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIRequestFactory

from audiofilesapi.models import song, audioBook, podcast, no_past
from audiofilesapi.viewsets import songViewset, audioBookViewset, podcastViewset

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


class createAudiobook(APITestCase):

    def test_audioBook(self):
        data = json.dumps(
            {"Title": "Outliers", "Author": "Gladwell Malcolm", "Narrator": "Michael Smith", "Duration": 500,
             "uploadTime": "2021-08-12T00:00"})
        response = self.client.post('/api/audiobook/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class getAudioBook_test(APITestCase):

    def test_view_set(self):
        request = APIRequestFactory().get("")
        audiobook_details = audioBookViewset.as_view({'get': 'retrieve'})
        audiobookFile = audioBook.objects.create(Title="Outliers", Author="Gladwell Malcolm", Narrator="Michael Smith",
                                                 Duration=500, uploadTime="2021-08-12T00:00")
        response = audiobook_details(request, pk=audiobookFile.pk)
        self.assertEqual(response.status_code, 200)


class UpdateSingleAudioBookTest(APITestCase):
    """ Test module for updating an existing audioBook record """

    def setUp(self):
        self.bookOne = audioBook.objects.create(Title="bookOne", Author="Gladwell Malcolms", Narrator="Michael Smith",
                                                Duration=500, uploadTime="2021-08-12T00:00")

        self.bookTwo = audioBook.objects.create(Title="bookTwo", Author="Gladwell Malcolm", Narrator="Michael Smith",
                                                Duration=500, uploadTime="2021-08-12T00:00")

        self.valid_payload = {
            'Title': 'bookOne',
            'Author': 'Gladwell Malcolms',
            'Narrator': 'Michael Smith',
            'Duration': 600,
            'uploadTime': '2021-08-12T00:00',
        }
        self.invalid_payload = {
            'Title': '',
            'Author': 'Gladwell Malcolms',
            'Narrator': 'Michael Smith',
            'Duration': 600,
            'uploadTime': '2021-08-12T00:00',
        }

    def test_valid_update_audioBook(self):
        edit_url = reverse('audiobook-detail', args=[self.bookOne.pk])
        response = self.client.patch(edit_url, data=json.dumps(self.valid_payload),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)


class DeleteSingleAudioBookTest(APITestCase):
    """ Test module for deleting an existing audiobook record """

    def setUp(self):
        self.bookOne = audioBook.objects.create(Title="bookOne", Author="Gladwell Malcolms", Narrator="Michael Smith",
                                                Duration=500, uploadTime="2021-08-12T00:00")

        self.bookTwo = audioBook.objects.create(Title="bookTwo", Author="Gladwell Malcolm", Narrator="Michael Smith",
                                                Duration=500, uploadTime="2021-08-12T00:00")

    def test_valid_delete_audioBook(self):
        edit_url = reverse('audiobook-detail', args=[self.bookOne.pk])
        response = self.client.delete(edit_url, kwargs={'pk': self.bookOne.pk})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_audioBook(self):
        edit_url = reverse('audiobook-detail', kwargs={'pk': 30})
        response = self.client.delete(edit_url, kwargs={'pk': 30})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


""" Test for the podcast endpoints """


class createPodcast(APITestCase):

    def test_Podcast(self):
        data = json.dumps(
            {"Name": "Clean Codes", "Duration": 500, "uploadTime": "2021-08-12T00:00", "Host": "Olusola",
             "Participant": "fifty people"})
        response = self.client.post('/api/podcast/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class getPodcast_test(APITestCase):

    def test_view_set(self):
        request = APIRequestFactory().get("")
        podcast_details = podcastViewset.as_view({'get': 'retrieve'})
        podcastFile = podcast.objects.create(Name="Clean Codes", Duration=500, uploadTime="2021-08-12T00:00",
                                             Host="Olusola", Participant="fifty people")
        response = podcast_details(request, pk=podcastFile.pk)
        self.assertEqual(response.status_code, 200)


class UpdateSinglePodcastTest(APITestCase):
    """ Test module for updating an existing podcast record """

    def setUp(self):
        self.podcastOne = podcast.objects.create(Name="Clean Codes", Duration=500, uploadTime="2021-08-12T00:00",
                                                 Host="Olusola", Participant="fifty people")

        self.podcastTwo = podcast.objects.create(Name="Clean Codes", Duration=500, uploadTime="2021-08-12T00:00",
                                                 Host="Olusola", Participant="fifty people")

        self.valid_payload = {
            'Name': 'Clean Codes',
            'Duration': 500,
            'uploadTime': '2021-08-12T00:00',
            'Host': 'Olusola',
            'Participant': 'fifty people',
        }
        self.invalid_payload = {
            'Name': '',
            'Duration': 500,
            'uploadTime': '2021-08-12T00:00',
            'Host': 'Olusola',
            'Participant': 'fifty people',
        }

    def test_valid_update_podcast(self):
        edit_url = reverse('podcast-detail', args=[self.podcastOne.pk])
        response = self.client.patch(edit_url, data=json.dumps(self.valid_payload),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)


class DeleteSinglePodcastTest(APITestCase):
    """ Test module for deleting an existing podcast record """

    def setUp(self):
        self.podcastOne = podcast.objects.create(Name="Clean Codes", Duration=500, uploadTime="2021-08-12T00:00",
                                                 Host="Olusola", Participant="fifty people")

        self.podcastTwo = podcast.objects.create(Name="Clean Codes", Duration=500, uploadTime="2021-08-12T00:00",
                                                 Host="Olusola", Participant="fifty people")

    def test_valid_delete_podcast(self):
        edit_url = reverse('podcast-detail', args=[self.podcastOne.pk])
        response = self.client.delete(edit_url, kwargs={'pk': self.podcastOne.pk})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_podcast(self):
        edit_url = reverse('podcast-detail', kwargs={'pk': 30})
        response = self.client.delete(edit_url, kwargs={'pk': 30})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class dateEntry_test(APITestCase):
    def test(self):
        value = utc.localize(datetime.datetime.today() - datetime.timedelta(days=5))
        with self.assertRaises(ValidationError):
            no_past(value)
