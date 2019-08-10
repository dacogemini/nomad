from django.db import models
from datetime import datetime
# from regions.models import Region


class Package(models.Model):
    # region = models.ForeignKey(Region, on_delete=models.DO_NOTHING)
    region = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    details = models.CharField(null=True, max_length=200)
    trip_id = models.URLField(max_length=128, db_index=True,
                              blank=True)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.details
