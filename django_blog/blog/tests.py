from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthTests(TestCase):
    def test_register_creates_user(self):
        resp = self.client.post(reverse('blog:register'), {
            'username': 'tester',
            'email': 'tester@example.com',
            'password1': 'ComplexPass123',
            'password2': 'ComplexPass123'
        })
        self.assertEqual(resp.status_code, 302)  # redirect after success
        self.assertTrue(User.objects.filter(username='tester').exists())

    def test_login(self):
        u = User.objects.create_user(username='loginuser', password='pwpass123')
        resp = self.client.post(reverse('blog:login'), {'username': 'loginuser', 'password': 'pwpass123'})
        self.assertEqual(resp.status_code, 302)  # redirect on success