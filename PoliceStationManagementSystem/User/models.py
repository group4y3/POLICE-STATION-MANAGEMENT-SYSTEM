from django.conf import settings
from django.contrib.auth.models import Group
from django.db import models

SEX_CHOICES = (
    ('male', 'MALE'),
    ('female', 'FEMALE'),

)


COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('brown','BROWN'),
    ('black','BLACK'),
    ('white', 'WHITE'),
)


class CrimeRecord(models.Model):
    CriminalID = models.IntegerField()
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Age = models.IntegerField()
    Sex = models.CharField(max_length=6, choices=SEX_CHOICES, default='male')
    Address = models.CharField(max_length=100)
    Height = models.CharField(max_length=6)
    EyeColor = models.CharField(max_length=6, choices=COLOR_CHOICES, default='black')
    Crime = models.CharField(max_length=100)
    PoliceStation = models.CharField(max_length=100)
    CriminalPhoto = models.FileField(upload_to='documents/%Y/%m/%d/', default='settings.MEDIA_ROOT/documents/download.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.CriminalID) + "==> " + str(self.FirstName) + " " + str(self.LastName) + " -- Police Station: " + str(self.PoliceStation)