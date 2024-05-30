from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch


class PostFetchTest(TestCase):

    @patch('requests.get')
    def test_fetch_post(self, mock_get):
        mock_get.return_value.json.return_value = {
            'userId': 1,
            'id': 1,
            'title': 'Test Title',
            'body': 'Test Body'
        }
        response = self.client.get(reverse('fetch_post'), {'fetch': '1'})
        self.assertRedirects(response, reverse('success'))
        self.assertEqual(self.client.session['posts'][0]['title'], 'Test Title')

    def test_success_view(self):
        session = self.client.session
        session['posts'] = [{'userId': 1, 'id': 1, 'title': 'Test Title', 'body': 'Test Body'}]
        session.save()
        response = self.client.get(reverse('success'))
        self.assertContains(response, 'Test Title')
        self.assertContains(response, 'Test Body')
