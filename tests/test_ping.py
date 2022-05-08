"""Test ping."""

# Standard libraries
import json

# Django
from django.urls import reverse


def test_ping(client):
    """Test ping function based views."""

    url = reverse('ping')
    response = client.get(url)
    content = json.loads(response.content)

    assert response.status_code == 200
    assert content['ping'] == 'pong!'
