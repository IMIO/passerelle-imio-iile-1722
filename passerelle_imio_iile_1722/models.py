import requests
from django.db import models
from passerelle.base.models import BaseResource
from passerelle.utils.api import endpoint
from passerelle.utils.jsonresponse import APIError
from requests import RequestException


class Iile1722(BaseResource):
    """
    Connecteur iMio - Iile 1722
    """

    url = models.URLField(
        max_length=255,
        blank=True,
        verbose_name="URL",
    )
    api_description = "Connecteur iMio - Iile 1722"
    category = "Connecteurs iMio"

    class Meta:
        verbose_name = "Connecteur Iile 1722"

    @property
    def session(self):
        session = requests.Session()
        session.headers.update(
            {
                "X-Api-Key": self.api_key,
                "Accept": "application/json",
            }
        )
        return session
