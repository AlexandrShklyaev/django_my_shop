import pytest


@pytest.mark.django_db
def test_selection_create(client, user, ad, test_token):
    expected_response = {
        'id': 1,
        'name': 'test_new_ads',
        'owner': user.id,
        'items': [ad.id]
    }

    response = client.post(
        "/selection/create/",
        {
            'name': 'test_new_ads',
            'owner': user.id,
            'items': [ad.id]
        },
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {test_token}"
    )

    assert response.status_code == 201
    assert response.data == expected_response
