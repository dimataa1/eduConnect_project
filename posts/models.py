from django.conf import settings
from django.db import models
from cloudinary.models import CloudinaryField


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

    image = CloudinaryField(
        'post_image',
        blank=True,
        null=True,
        default="static/default/default.png",
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

    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"


    @property
    def rating(self) -> int:
        return self.up_votes - self.down_votes

    def update_rating(self, action):
        if action == 'upvote':
            self.up_votes += 1
        elif action == 'downvote':
            self.down_votes += 1
        self.save()
        return self.rating

    @rating.setter
    def rating(self, value):
        self._rating = value

    def has_user_voted(self, user):
        return Vote.objects.filter(user=user, comment=self).exists()


class School(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="schools",
    )
    name = models.CharField(
        max_length=255
    )

    town = models.CharField(
        max_length=255
    )

    description = models.TextField()

    image = CloudinaryField(
        'school_image',
        blank=True,
        null=True,
        default="static/default/default.png",
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    vote_type = models.CharField(
        max_length=10,
        choices=(('upvote', 'Upvote'), ('downvote', 'Downvote'))
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'comment')


class Tour(models.Model):
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name='tours',
    )
    name = models.CharField(
        max_length=255,
        help_text="The name of the tour.",
    )
    description = models.TextField()

    date = models.DateTimeField()

    location = models.CharField(
        max_length=255,
        help_text="The location of the tour.",
    )
    image = CloudinaryField(
        'tour_image',
        blank=True,
        null=True,
        default="static/default/default.png",
    )
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='scheduled_tours',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"Tour: {self.name} for {self.school.name} on {self.date.strftime('%Y-%m-%d')}"
