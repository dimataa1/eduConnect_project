from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to="static/post_images/",
        blank=True,
        null=True
    )

    subject = models.CharField(
        max_length=100
    )

    grade = models.CharField(
        max_length=50
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"


class School(models.Model):
    name = models.CharField(
        max_length=255
    )

    town = models.CharField(
        max_length=255
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to='static/school_images/',
        blank=True, null=True
    )

    def __str__(self):
        return self.name
