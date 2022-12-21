import json
from django.test import  TestCase
from rest_framework.test import APIClient
from titles.models import Title
from rest_framework import status
class TitlesTestCase(TestCase):

    title_dict = {"title_id": "USD", "title": "DOLAR", "clasification": "DIV", "value": "500.000.000", "creation_date": "2022-03-14", "expiration_date": "2023-03-15","fee_paid": "y"}
    title2_dict = {"title_id": "TRPV", "title": "TÍTULO DE PARTICIPACIÓN RENTA VARIABLE", "value": "256.000.000", "creation_date": "2022-08-25", "expiration_date": "2023-08-26","fee_paid": "y"}
    title3_dict = {"title_id": "TP", "title": "TITULO DE PARTICIPACIÓN", "value": "360.000.000", "creation_date": "2022-02-16", "expiration_date": "2023-02-17","fee_paid": "y"}
    title4_dict = {"title_id": "USD", "title": "DOLAR", "clasification": "DIV", "value": "500.000.000", "creation_date": "2022-03-14", "expiration_date": "2023-03-15","fee_paid": "n"}
    title5_dict = {"title_id": "USD", "title": "DOLAR", "clasification": "DIV", "value": "500.000.000", "creation_date": "2022-01-25", "expiration_date": "2023-03-15","fee_paid": "y"}

    def test_create_title(self):
        response = APIClient().post('/titles/', data=self.title_dict, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Title.objects.first().title_id == "USD"


    def test_titles_quantity(self):
        Title.objects.create(**self.title_dict)
        Title.objects.create(**self.title2_dict)
        Title.objects.create(**self.title3_dict)
        response = APIClient().get('/titles/quantity/')
        result = json.loads(response.data)
        assert response.status_code == status.HTTP_200_OK
        assert result['quantity'] == 3

    def test_change_fee_paid(self):
        Title.objects.create(**self.title4_dict)
        title_instance = Title.objects.all().first()
        assert title_instance.fee_paid == 'n'
        response = APIClient().put(f'/titles/?title_id={title_instance.title_id}', {'fee_paid': 'y'}, format='json')
        title_instance.refresh_from_db()
        assert response.status_code == status.HTTP_200_OK
        assert title_instance.fee_paid == 'y'

    def test_change_creation_date(self):
        Title.objects.create(**self.title5_dict)
        title_instance = Title.objects.all().first()
        response = APIClient().put(f'/titles/?creation_date=2022-01-25', {'creation_date': '2022-02-01'}, format='json')
        title_instance.refresh_from_db()
        assert response.status_code == status.HTTP_200_OK
        assert str(title_instance.creation_date) == '2022-02-01'
 
    def test_eliminate_title(self):
        Title.objects.create(**self.title_dict)
        title_id = Title.objects.all().first().title_id
        response = APIClient().delete(f'/titles/?title_id={title_id}')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Title.objects.all().first() == None

    def test_get_titles(self):
        Title.objects.create(**self.title_dict)
        Title.objects.create(**self.title2_dict)
        Title.objects.create(**self.title3_dict)
        response = APIClient().get('/titles/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3
