import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_create(client, user, category):
    ad_last = AdFactory.create()  # найдем последний ид (он мб не равен 1)

    expected_response = {
        'id': ad_last.id + 1,
        'name': 'test_new_ads',
        'price': 100,
        'description': 'test',
        'image': None,
        'is_published': False,
        'author': user.id,
        'category': category.id
    }

    response = client.post(
        "/ad/create/",
        {
            "name": "test_new_ads",
            "price": 100,
            "description": "test",
            "is_published": False,
            "author": user.id,
            "category": category.id
        },
        content_type="application/json"
    )
    print(category.name,"--", category.slug)
    assert response.status_code == 201
    assert response.data == expected_response
