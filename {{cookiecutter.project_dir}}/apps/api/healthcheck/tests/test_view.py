import pytest


def test_view(client):
    response = client.get('/__health')
    assert response.status_code == 200
    assert b'good' in response.content
