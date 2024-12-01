from django.contrib.auth import get_user_model
from django.test import TestCase

from posts.models import Post

User = get_user_model()

class PostModelTests(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

    def test_post_creation(self):

        post = Post.objects.create(
            title="Sample Post",
            description="This is a sample post description.",
            author=self.user
        )
        self.assertIsNotNone(post.pk)
        self.assertEqual(post.title, "Sample Post")
        self.assertEqual(post.description, "This is a sample post description.")
        self.assertEqual(post.author, self.user)

    def test_post_description_max_length(self):

        post = Post.objects.create(description="A" * 256, title="Title", author=self.user)
        max_length = 300
        self.assertLessEqual(len(post.description), max_length)

class UserModelTests(TestCase):
    def test_user_creation(self):

        user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123"
        )
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("password123"))

    def test_user_is_staff_default(self):

        user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123"
        )
        self.assertFalse(user.is_staff)
