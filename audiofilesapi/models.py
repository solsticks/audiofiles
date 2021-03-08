from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
import pytz

utc = pytz.UTC


# Create your models here.
def no_past(value):
    today = utc.localize(datetime.now())
    if value < today:
        raise ValidationError('Date cannot be in the past')


class song(models.Model):
    Name = models.CharField(max_length=100)
    Duration = models.IntegerField()
    uploadTime = models.DateTimeField(validators=[no_past])

    def __DateTime__(self):
        self.uploadTime = datetime.now()


class podcast(models.Model):
    Name = models.CharField(max_length=100)
    Duration = models.IntegerField()
    uploadTime = models.DateTimeField(validators=[no_past])
    Host = models.CharField(max_length=100)
    Participant = models.CharField(max_length=100, blank=True)

    def __DateTime__(self):
        self.uploadTime = datetime.now()


class audioBook(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Narrator = models.CharField(max_length=100)
    Duration = models.IntegerField()
    uploadTime = models.DateTimeField(validators=[no_past])

    def __DateTime__(self):
        self.uploadTime = datetime.now()
