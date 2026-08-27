import json

from django.db import models
from passerelle.base.models import BaseResource
from passerelle.utils.api import endpoint

from .utils import build_intervention_multipart


class Iile1722(BaseResource):
    """
    Connecteur iMio - Iile 1722

    Reçoit le fichier XML d'intervention envoyé en JSON/base64 par l'action
    de workflow wcs « Envoi intervention 1722 » et le retransmet au
    ServeurSGO IILE (CU112messages) au format multipart/form-data, seul
    format accepté par ce dernier (voir rapport-integration-iile-1722.md).
    """

    url = models.URLField(
        max_length=255,
        blank=False,
        verbose_name="URL",
        help_text=(
            "URL complète du endpoint ServeurSGO cible, ex : "
            "https://test-guichetcitoyen.iile.be/ServeurSGO/resources/CU112messages"
        ),
    )
    api_description = "Connecteur iMio - Iile 1722"
    category = "Connecteurs iMio"

    # Le ServeurSGO (Glassfish) peut être lent à répondre ; sans cet
    # attribut, les appels via self.requests héritent du timeout par
    # défaut (5 s) imposé par settings.ENDPOINT_REQUESTS_TIMEOUT.
    requests_timeout = 30

    class Meta:
        verbose_name = "Connecteur Iile 1722"

    @endpoint(
        name="send-intervention",
        perm="can_access",
        description="Transmet une intervention 1722 au ServeurSGO IILE",
        methods=["post"],
        parameters={},
        long_description=(
            "Reçoit le fichier XML de l'intervention, envoyé en JSON/base64 par "
            "l'action de workflow wcs « Envoi intervention 1722 », et le "
            "retransmet au ServeurSGO IILE au format multipart/form-data."
        ),
        display_category="Intervention 1722",
    )
    def send_intervention(self, request):
        post_data = json.loads(request.body)
        files = build_intervention_multipart(post_data)

        response = self.requests.post(self.url, files=files)

        return {
            "status_code": response.status_code,
            "data": response.text,
        }
