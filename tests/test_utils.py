import base64

import pytest

from passerelle_imio_iile_1722.utils import build_intervention_multipart


def test_build_intervention_multipart_base64():
    payload = {
        "content": {
            "filename": "mission",
            "content_type": "text/xml",
            "content": base64.b64encode(b"<intervention/>").decode(),
            "content_is_base64": True,
        }
    }

    files = build_intervention_multipart(payload)

    assert list(files.keys()) == ["content"]
    filename, content, content_type = files["content"]
    assert filename == "mission"
    assert content == b"<intervention/>"
    assert content_type == "text/xml"


def test_build_intervention_multipart_not_base64():
    payload = {
        "content": {
            "filename": "mission",
            "content_type": "text/xml",
            "content": "<intervention/>",
            "content_is_base64": False,
        }
    }

    _, content, _ = build_intervention_multipart(payload)["content"]

    assert content == b"<intervention/>"


def test_build_intervention_multipart_default_content_type():
    payload = {
        "content": {
            "filename": "mission",
            "content": base64.b64encode(b"data").decode(),
            "content_is_base64": True,
        }
    }

    _, _, content_type = build_intervention_multipart(payload)["content"]

    assert content_type == "application/octet-stream"


def test_build_intervention_multipart_missing_field_raises():
    with pytest.raises(KeyError):
        build_intervention_multipart({})
