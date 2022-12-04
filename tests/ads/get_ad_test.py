import pytest

from ads.serializers import AdDetailSerializer


@pytest.mark.django_db
def test_ad_retrieve(client, ad, test_token):
    response = client.get(
        f"/ad/{ad.id}/",
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {test_token}")

    assert response.status_code == 200
    assert response.data == AdDetailSerializer(ad).data
