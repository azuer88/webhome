from django.db import models

# Create your models here.


class File(models.Model):
    IMAGE_FILE = 1
    VIDEO_FILE = 2
    AUDIO_FILE = 3
    OTHER_FILE = 4
    FILE_CHOICES = (
        (IMAGE_FILE, "Image"),
        (VIDEO_FILE, "Video"),
        (AUDIO_FILE, "Audio"),
        (OTHER_FILE, "Other"),
    )

    name = models.CharField(max_length=30, unique=True, default='')
    filename = models.FileField(upload_to='files/')
    filetype = models.SmallIntegerField(choices=FILE_CHOICES, default=1)

    def __unicode__(self):
        return u"{} ({})".format(self.name, self.get_filetype_display())
