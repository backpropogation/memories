from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from apps.memories.factory import MemoryFactory
from apps.users.factory import UserFactory


class MemoriesTests(APITestCase):
    def setUp(self):
        self.user_owner = UserFactory.create()
        Token.objects.create(user=self.user_owner)
        self.user_not_owner = UserFactory.create()
        Token.objects.create(user=self.user_not_owner)
        self.user_owner_memories_count = 10
        self.user_not_owner_memories_count = 0
        self.view_basename = 'memory-list'
        self.memory_data = {
            'title': 'Memory_0',
            'description': 'Film great activity law economy last. Cover star talk night.',
            'longitude': 10.12312,
            'latitude': 10.12312,
        }
        self.bad_memory_data = {
            'title': 'Memory_0',
            'description': 'Film great activity law economy last. Cover star talk night.',
        }

    def test_get_right_memories_count(self):
        """
        Ensure user gets right count of memories.
        """
        memories = MemoryFactory.create_batch(size=self.user_owner_memories_count, owner=self.user_owner)
        url = reverse(self.view_basename)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user_owner.auth_token.key}')
        data = self.client.get(url).data
        self.assertEqual(self.user_owner_memories_count, len(data))

    def test_get_other_user_memories(self):
        """
        Ensure user gets only his memories.
        """
        MemoryFactory.create_batch(size=self.user_not_owner_memories_count, owner=self.user_owner)
        url = reverse('memory-list')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user_not_owner.auth_token.key}')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertNotEqual(self.user_owner_memories_count, len(response.data))

    def test_create_memory_with_credentials(self):
        """
        Ensure memory can be created by user only authenticated.
        """

        url = reverse(self.view_basename)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user_owner.auth_token.key}')
        response = self.client.post(url, self.memory_data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, len(response.data))

    def test_create_memory_without_credentials(self):
        """
        Ensure memory can not be created by anonymous user.
        """

        url = reverse(self.view_basename)
        response = self.client.post(url, self.memory_data)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_create_memory_with_bad_data(self):
        """
        Ensure memory can not be created without all required fields.
        """

        url = reverse(self.view_basename)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user_owner.auth_token.key}')
        response = self.client.post(url, self.bad_memory_data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
