import base64


def build_intervention_multipart(payload, field_name="content"):
    """
    Convertit le payload JSON envoyé par l'action de workflow wcs
    « webservice_call » (qui encode systématiquement un fichier joint en
    base64, quelle que soit sa nature) en dictionnaire "files" utilisable
    par `requests` pour un envoi HTTP multipart/form-data.

    Le ServeurSGO IILE (Glassfish) n'accepte que ce format de transport
    pour les interventions 1722 (voir rapport-integration-iile-1722.md,
    section 4) : un envoi JSON est systématiquement rejeté en 415 avant
    tout traitement du contenu.

    payload attendu (tel qu'envoyé par wcs) :
    {
        "content": {
            "filename": "mission",
            "content_type": "text/xml",
            "content": "<base64>",
            "content_is_base64": true
        }
    }
    """
    attachment = payload[field_name]

    raw_content = attachment["content"]
    if attachment.get("content_is_base64", False):
        file_content = base64.b64decode(raw_content)
    else:
        file_content = raw_content.encode("utf-8")

    return {
        field_name: (
            attachment["filename"],
            file_content,
            attachment.get("content_type", "application/octet-stream"),
        )
    }
