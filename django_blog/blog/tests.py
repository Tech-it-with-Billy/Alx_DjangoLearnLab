from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

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

class PostCRUDTests(TestCase):
    def setUp(self):
        # create two users
        self.author = User.objects.create_user(username='author', password='pass12345')
        self.other = User.objects.create_user(username='other', password='pass12345')

        # create a post
        self.post = Post.objects.create(title='Test Post', content='Some content', author=self.author)

    def test_post_list_view(self):
        resp = self.client.get(reverse('blog:post-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Test Post')

    def test_post_detail_view(self):
        resp = self.client.get(reverse('blog:post-detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Some content')

    def test_create_requires_login(self):
        resp = self.client.get(reverse('blog:post-create'))
        # should redirect to login
        self.assertNotEqual(resp.status_code, 200)
        self.client.login(username='author', password='pass12345')
        resp = self.client.get(reverse('blog:post-create'))
        self.assertEqual(resp.status_code, 200)

    def test_author_can_edit(self):
        self.client.login(username='author', password='pass12345')
        resp = self.client.post(reverse('blog:post-update', kwargs={'pk': self.post.pk}), {
            'title': 'Updated title',
            'content': 'Updated content'
        })
        # redirect after successful update
        self.assertEqual(resp.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated title')

    def test_non_author_cannot_edit(self):
        self.client.login(username='other', password='pass12345')
        resp = self.client.get(reverse('blog:post-update', kwargs={'pk': self.post.pk}))
        # should be forbidden (403) or redirect; UserPassesTestMixin defaults to 403
        self.assertIn(resp.status_code, (302, 403,))  # allow redirect-to-login or 403

    def test_author_can_delete(self):
        self.client.login(username='author', password='pass12345')
        resp = self.client.post(reverse('blog:post-delete', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 302)
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())

