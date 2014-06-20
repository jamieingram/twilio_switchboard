from django.db import models
from django.contrib.auth.models import User

from ..models import BaseModel
# Create your models here.


class Visitor(BaseModel):
    user = models.ForeignKey(User,
                             verbose_name='User')
    access_code = models.CharField(max_length=6, blank=False, unique=True)

    def __unicode__(self):
        return self.user.username


class Recording(BaseModel):
    description = models.CharField(max_length=200, blank=False, default='')
    audio_file = models.FileField(upload_to='audio',
                                  help_text='Audio mp3 file',
                                  default='',
                                  blank=True)
    message = models.TextField(blank=True, default='')
    from_number = models.CharField(max_length=6, blank=True)
    from_name = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.description


class Message(BaseModel):
    # a message links a user with a particular visitor
    recording = models.ForeignKey(Recording,
                                  verbose_name='Recording',
                                  related_name='+',
                                  blank=True)
    recipient = models.ForeignKey(Visitor,
                                  verbose_name='Recipient',
                                  related_name='+',
                                  blank=False)
    sender = models.ForeignKey(Visitor,
                               verbose_name='Sender',
                               related_name='+',
                               blank=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    accessed = models.BooleanField(default=False)
