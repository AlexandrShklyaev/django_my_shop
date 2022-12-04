import pytest

from ads.models import Ad, Category
from users.models import User

@pytest.mark.django_db
def test_ads_list(client):
    user_test = User.objects.create(

            username= "test",
            password="test",
            first_name= "test",
            last_name= "test",
            role= "member",
            age= 20,
            email= "test@test.ru"
    )

    cat_test = Category.objects.create(name="test",slag="test")

    ad = Ad.objects.create(
        name="test",
        author = user_test,
        price = 100,
        description = "",
        is_published = True,
        category = cat_test,
        image=None
    )
    exprcted_response = {
        "count" : 1,
        "next" : None,
        "previous" : None,
        "results":[{
            'id' : ad.pk,
            'name' : 'test',
            'author' : user_test.username,
            'price' : 100,
            'description' : '',
            'is_published' : True,
            'category' : cat_test.name,
            'image' : None
        }]
    }
    response = client.get("/ad/")

    assert response.status_code == 200
    assert response.data == exprcted_response