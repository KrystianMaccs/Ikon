from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedUUIDModel
from apps.profiles.models import Profile


class Booking(TimeStampedUUIDModel):
    event = models.CharField(max_length=120)
    client = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="bookings")
    photographer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="booked_by")
    booking_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=120)