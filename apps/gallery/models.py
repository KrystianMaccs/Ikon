from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedUUIDModel
from apps.profiles.models import Profile


User = get_user_model()

class Album(TimeStampedUUIDModel):
    name = models.CharField(_("Album Name"), max_length=255)
    description = models.TextField(_("Album Description"), blank=True, null=True)
    photographer = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="profile", verbose_name=_("Photographer")
    )
    image = models.ImageField(_("Album"), upload_to="albums/")
    is_public = models.BooleanField(_("Is Public"), default=False)

    class Meta:
        verbose_name = _("Album")
        verbose_name_plural = _("Albums")
        ordering = ["name"]


    def __str__(self):
        return self.name
    
class Photo(TimeStampedUUIDModel):
    name = models.CharField(_("Photo Name"), max_length=255)
    description = models.TextField(_("Photo Description"), blank=True, null=True)
    image = models.ImageField(_("Photo"), upload_to="photos/")
    is_public = models.BooleanField(_("Is Public"), default=False)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="photos", verbose_name=_("Owner")
    )
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name="photos", related_query_name="photo", verbose_name=_("Albums")
    )

    class Meta:
        verbose_name = _("Photo")
        verbose_name_plural = _("Photos")
        ordering = ["name"]

    def __str__(self):
        return self.name
