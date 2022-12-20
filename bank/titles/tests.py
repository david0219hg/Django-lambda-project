from django.test import  TestCase
from rest_framework.test import APIClient
from titles.models import Title
class TitlesTestCase(TestCase):

    def test_create_title(self):
        title_dict = {"title_id": "USD", "title": "DOLAR", "clasification": "DIV", "value": "500.000.000", "created_date": "2022-03-14", "expiration_date": "2023-03-15","fee_paid": "y"}
        request = APIClient().post('/titles/register/', data=title_dict, format='json')
        print(request.status_code)
        assert request.status_code == 201
        assert Title.objects.first().title_id == "USD"
    
