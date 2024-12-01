from django.test import TestCase
from posts.forms import PostForm, SchoolForm, CommentForm
from django.contrib.auth import get_user_model

User = get_user_model()

class PostFormTests(TestCase):
    def setUp(self):
        # Create a user instance for testing
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123"
        )

    def test_valid_post_form(self):
        form_data = {
            'title': 'Valid Post Title',
            'description': 'This is a valid description for a post.',
            'image': None,
            'subject': 'Mathematics',
            'grade': '10',
        }
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_post_form_missing_required_field(self):
        form_data = {
            'title': '',  # Missing title
            'description': 'This is a sample description.',
            'image': None,
            'subject': 'Science',
            'grade': '11',
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)


class CommentFormTests(TestCase):
    def test_comment_form_invalid_empty_content(self):
        # Create a dictionary with an empty content field (assuming it's required)
        form_data = {
            'content': '',  # Invalid: `content` should not be empty if `blank=False`
        }
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)
