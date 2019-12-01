from django.conf import settings
from django.db import models


class CoordinatesRestriction:
    MAX_DIGITS_LAT = 22
    MAX_DEC_PLACES_LAT = 20
    MAX_DIGITS_LON = 23
    MAX_DEC_PLACES_LON = 20


class Memory(models.Model):
    """
    Main entity  of the app that represents memory.
    """

    title = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Title of the memory'
    )
    description = models.TextField(
        max_length=1000,
        verbose_name='Description of the memory'
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Owner of the memory'
    )
    longitude = models.DecimalField(
        max_digits=CoordinatesRestriction.MAX_DIGITS_LON,
        decimal_places=CoordinatesRestriction.MAX_DEC_PLACES_LON,
        verbose_name='Longitude'
    )
    latitude = models.DecimalField(
        max_digits=CoordinatesRestriction.MAX_DIGITS_LAT,
        decimal_places=CoordinatesRestriction.MAX_DEC_PLACES_LAT,
        verbose_name='Latitude'
    )
    posted_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Time the memory has been posted.'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-posted_at',)
