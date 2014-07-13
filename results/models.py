from django.db import models
from django.contrib.auth.models import AbstractUser

# from django.utils import datetime_safe
import datetime
from datetime import datetime, timedelta, date
import time
# Create your models here.

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

class User(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    address1 = models.CharField(max_length=120, blank=True)
    address2 = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=120, blank=True)
    state = models.CharField(max_length=120, blank=True)
    zip = models.CharField(max_length=120, blank=True)
    country = models.CharField(max_length=120, blank=True)
    club = models.ForeignKey(Club, related_name="home_club", null=True, blank=True)
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)


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
        return "{} - {}".format(self.date, self.name)


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


class Biathlete(models.Model):
    # THESE DATES SHOULD BE datetime.now - datetime year, etc. of enter date to ageclass
    # currently set to oldest age for class
    BOY10 = 10
    BOY12 = 12
    BOY14 = 14
    BOY16 = 16
    BOYS = 16
    YM = 18
    JM = 20
    SM = 29
    MM = 44
    SMM = 99
    GIRL10 = 10
    GIRL12 = 12
    GIRL14 = 14
    GIRL16 = 16
    GIRLS = 16
    YW = 18
    JW = 20
    SW = 29
    MW = 44
    SMW = 99

    age_class = {
        'BOY10': "Boys under 10",
        'BOY12': "Boys under 12",
        'BOY14': "Boys under 14",
        'BOY16': "Boys under 16",
        'BOYS': "Boys under 16",
        'YM': "Youth Men",
        'JM': "Junior Men",
        'SM': "Men",
        'MM': "Masters Men",
        'SMM': "Senior Masters Men",
        'GIRL10': "Girls under 10",
        'GIRL12': "Girls under 12",
        'GIRL14': "Girls under 14",
        'GIRL16': "Girls under 16",
        'GIRLS': "Girls under 16",
        'YW': "Youth Women",
        'JW': "Junior Women",
        'SW': "Women",
        'MW': "Masters Women",
        'SMW': "Senior Masters Women",
    }



class Result(models.Model):
    racer = models.ForeignKey(Racer, related_name="racer")
    race = models.ForeignKey(Race, related_name="race")
    start_time = models.CharField(max_length=120)
    finish_time = models.CharField(max_length=120)
    place = models.SmallIntegerField()
    first_shoot = models.SmallIntegerField(blank=True)
    second_shoot = models.SmallIntegerField(blank=True)
    third_shoot = models.SmallIntegerField(blank=True)
    fourth_shoot = models.SmallIntegerField(blank=True)

    # def get_split_time(self):
    #     # return timedelta
    #     if self.start_time is None or self.start_time == "":
    #         return (datetime(self.finish_time)) - (datetime(self.race.start_time))
    #     else:
    #         return (datetime(self.finish_time)) - (datetime(self.start_time))
    #
    # def get_race_age(self):
    #     return self.race.date - self.racer.birthdate


    def __unicode__(self):
        return "{}:\t{}. {} \t{}\t".format(self.race, self.place, self.racer, self.finish_time)
        # return "{}. {} \t{}".format(self.place, self.racer, self.race, self.get_split_time())

class CustomResultField(models.Model):
    custom_result_name = models.CharField(max_length=120)
    custom_result_value = models.CharField(max_length=120, blank=True)
    custom_result = models.ForeignKey(Result, related_name="custom_result")