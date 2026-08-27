# passerelle-imio-iile-1722

Connecteur iMio - Iile 1722

Reçoit le fichier XML d'une intervention 1722 envoyé en JSON/base64 par
l'action de workflow wcs « Envoi intervention 1722 » et le retransmet au
ServeurSGO IILE (`CU112messages`) au format `multipart/form-data`, seul
format accepté par ce dernier. Voir `rapport-integration-iile-1722.md`
pour le détail du diagnostic ayant mené à ce connecteur.

## Installation

- ajouter aux applications installées de Passerelle :
  `INSTALLED_APPS += ('passerelle_imio_iile_1722',)`

## Configuration

- créer un connecteur « Iile 1722 » et renseigner le champ **URL** avec
  l'URL complète du endpoint ServeurSGO cible, par exemple :
  - test : `https://test-guichetcitoyen.iile.be/ServeurSGO/resources/CU112messages`
  - prod : `https://guichet-citoyen.iile.be/ServeurSGO/resources/CU112messages`

## Utilisation

Dans wcs, configurer l'action de workflow `webservice_call` pour qu'elle
POST vers l'endpoint `send-intervention` du connecteur, avec le corps
JSON habituel `{"content": {{form_attachments_mission}} }`. Le connecteur
décode le contenu base64 et le relaie en multipart au ServeurSGO IILE.

## Tests

```
pip install pytest
pytest
```
