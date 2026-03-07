from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import Client, TestCase

from core.services.agents.openclow import OpenClowError


class OpenClowAgentViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')

    def test_login_required(self):
        response = self.client.post('/agents/openclow/', {'prompt': 'hello'})
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_method_not_allowed_for_get(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/agents/openclow/')

        self.assertEqual(response.status_code, 405)

    def test_prompt_required(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post('/agents/openclow/', {'prompt': ''})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], 'Prompt is required.')

    @patch('core.views.ask_openclow', return_value='hi from openclow')
    def test_success_response(self, mock_openclow):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post('/agents/openclow/', {'prompt': 'say hi'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['answer'], 'hi from openclow')
        mock_openclow.assert_called_once_with('say hi')

    @patch('core.views.ask_openclow', side_effect=Exception('boom'))
    def test_unexpected_exception_propagates(self, _mock_openclow):
        self.client.login(username='testuser', password='testpass123')

        with self.assertRaises(Exception):
            self.client.post('/agents/openclow/', {'prompt': 'say hi'})

    @patch('core.views.ask_openclow', side_effect=OpenClowError('upstream failed'))
    def test_upstream_error(self, _mock_openclow):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post('/agents/openclow/', {'prompt': 'say hi'})

        self.assertEqual(response.status_code, 502)
        self.assertEqual(response.json()['error'], 'upstream failed')


class OpenClowServiceTests(TestCase):
    @patch('core.services.agents.openclow.settings.OPENCLOW_API_TOKEN', '')
    def test_missing_token(self):
        from core.services.agents.openclow import OpenClowError, ask_openclow

        with self.assertRaises(OpenClowError):
            ask_openclow('hello')
