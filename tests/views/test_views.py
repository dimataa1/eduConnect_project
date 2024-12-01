from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from posts.models import Post

User = get_user_model()

class PostViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123"
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_structure/post_list.html')

    def test_post_detail_view(self):
        post = Post.objects.create(
            title="Sample Post",
            description="Description",
            author=self.user
        )
        response = self.client.get(reverse('post_detail', kwargs={'pk': post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_structure/post_detail.html')

    def test_post_create_view(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post(reverse('new_post'), {
            'title': 'New Post',
            'description': 'New description'
        })
        self.assertEqual(response.status_code, 200)

    def test_post_delete_view(self):
        post = Post.objects.create(
            title="Sample Post",
            description="Description",
            author=self.user
        )
        response = self.client.post(reverse('post_delete', kwargs={'pk': post.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(pk=post.pk).exists())

class UserViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123"
        )

    def test_user_dashboard_view(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/dashboard.html')

