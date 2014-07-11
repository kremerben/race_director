from django.db import models
from django.contrib.auth.models import AbstractUser

# from django.utils import datetime_safe
import datetime
from datetime import datetime, timedelta, date
import time
# Create your models here.

class User(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    address1 = models.CharField(max_length=120, blank=True)
    address2 = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=120, blank=True)
    state = models.CharField(max_length=120, blank=True)
    zip = models.CharField(max_length=120, blank=True)
    country = models.CharField(max_length=120, blank=True)


class BaseModel(models.Model):
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name


class Club(BaseModel):
    region = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    website = models.URLField(max_length=120, null=True, blank=True)
    contact_name = models.CharField(max_length=120)
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=120, blank=True)


class RaceSeries(BaseModel):
    description = models.TextField()
    contact_name = models.CharField(max_length=120)
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=120, blank=True)
    info_document = models.FileField(upload_to='uploads/', null=True, blank=True)
    website = models.URLField(max_length=120, null=True, blank=True)
    host_club = models.ForeignKey(Club, related_name="host_club", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Race Series"


class Race(BaseModel):
    date = models.DateField(default=(date.today() + timedelta(days=14)))
    start_time = models.TimeField(default="10:00")
    location = models.CharField(max_length=120)
    fee = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    contact_name = models.CharField(max_length=120)
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=120, blank=True)
    info_document = models.FileField(upload_to='uploads/', null=True, blank=True)
    result_document = models.FileField(upload_to='uploads/', null=True, blank=True)
    website = models.URLField(max_length=120, null=True, blank=True)
    race_series = models.ForeignKey(RaceSeries, related_name="race_series", null=True, blank=True)

    def __unicode__(self):
        return "{} - {}".format(self.name, self.date)


class Racer(BaseModel):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthdate = models.DateField(null=True, blank=True)
    club = models.ForeignKey(Club, related_name="racer_club", null=True, blank=True)
    hometown = models.CharField(max_length=120, blank=True)
    user = models.OneToOneField(User, null=True, blank=True)

    def current_age(self):
        birthday = time.strptime(self.birthdate)
        return datetime.now() - datetime(birthday)

    def calculate_age(self):
        today = date.today()
        return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))

    age = property(calculate_age)

class Result(models.Model):
    racer = models.ForeignKey(Racer, related_name="racer")
    race = models.ForeignKey(Race, related_name="race")
    start_time = models.DateTimeField(default="9:00")
    finish_time = models.DateTimeField()
    place = models.IntegerField()

    def get_split_time(self):
        # return timedelta
        if self.start_time is None or self.start_time == "":
            return (datetime(self.finish_time)) - (datetime(self.race.start_time))
        else:
            return (datetime(self.finish_time)) - (datetime(self.start_time))

    def get_race_age(self):
        return self.race.date - self.racer.birthdate


    def __unicode__(self):
        return "{}:\t{}. {} \t{}\t".format(self.race, self.place, self.racer, self.finish_time)
        # return "{}. {} \t{}".format(self.place, self.racer, self.race, self.get_split_time())

class CustomResultField(BaseModel):
    custom_field_value = models.CharField(max_length=120, blank=True)
    custom_result = models.ForeignKey(Result, related_name="custom_result")