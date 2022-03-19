import json
from datetime import datetime

import factory
from django.core import management
from django.test import TestCase
from django.urls import reverse
from faker import Factory
from rest_framework import status
from rest_framework.test import APIClient

from ..models import User
from .factories import UserFactory

faker = Factory.create()


class User_Test(TestCase):
    def setUp(self):
        self.api_client = APIClient()
        UserFactory.create_batch(size=3)

    def test_create_user(self):
        """
        Ensure we can create a new user object.
        """
        client = self.api_client
        user_count = User.objects.count()
        user_dict = factory.build(dict, FACTORY_CLASS=UserFactory)
        response = client.post(reverse('user-list'), user_dict)
        created_user_pk = response.data['id']
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.count() == user_count + 1
        user = User.objects.get(pk=created_user_pk)

        assert user_dict['role'] == user.role
        assert user_dict['nationality'] == user.nationality
        assert user_dict['gender'] == user.gender

    def test_get_one(self):
        client = self.api_client
        user_pk = User.objects.first().pk
        user_detail_url = reverse('user-detail', kwargs={'pk': user_pk})
        response = client.get(user_detail_url)
        assert response.status_code == status.HTTP_200_OK

    def test_fetch_all(self):
        """
        Create 3 objects, do a fetch all call and check if you get back 3 objects
        """
        client = self.api_client
        response = client.get(reverse('user-list'))
        assert response.status_code == status.HTTP_200_OK
        assert User.objects.count() == len(response.data)

    def test_delete(self):
        """
        Create 3 objects, do a fetch all call and check if you get back 3 objects.
        Then in a loop, delete one at a time and check that you get the correct number back on a fetch all.
        """
        client = self.api_client
        user_qs = User.objects.all()
        user_count = User.objects.count()

        for i, user in enumerate(user_qs, start=1):
            response = client.delete(reverse('user-detail', kwargs={'pk': user.pk}))
            assert response.status_code == status.HTTP_204_NO_CONTENT
            assert user_count - i == User.objects.count()

    def test_update_correct(self):
        """
        Add an object. Call an update with 2 (or more) fields updated.
        Fetch the object back and confirm that the update was successful.
        """
        client = self.api_client
        user_pk = User.objects.first().pk
        user_detail_url = reverse('user-detail', kwargs={'pk': user_pk})
        user_dict = factory.build(dict, FACTORY_CLASS=UserFactory)
        response = client.patch(user_detail_url, data=user_dict)
        assert response.status_code == status.HTTP_200_OK

        assert user_dict['role'] == response.data['role']
        assert user_dict['nationality'] == response.data['nationality']
        assert user_dict['gender'] == response.data['gender']

    def test_update_role_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        user = User.objects.first()
        user_detail_url = reverse('user-detail', kwargs={'pk': user.pk})
        user_role = user.role
        data = {
            'role': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(user_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert user_role == User.objects.first().role

    def test_update_nationality_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        user = User.objects.first()
        user_detail_url = reverse('user-detail', kwargs={'pk': user.pk})
        user_nationality = user.nationality
        data = {
            'nationality': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(user_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert user_nationality == User.objects.first().nationality

    def test_update_gender_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        user = User.objects.first()
        user_detail_url = reverse('user-detail', kwargs={'pk': user.pk})
        user_gender = user.gender
        data = {
            'gender': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(user_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert user_gender == User.objects.first().gender
