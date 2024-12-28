from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    CATEGORY_CHOICES = [
        ('TECH', 'Technology'),
        ('ENT', 'Entertainment'),
        ('BUS', 'Business'),
        ('LIFE', 'Lifestyle'),
        ('FOOD', 'Food'),
        ('TRAV', 'Travel'),
        ('OTHER', 'Other'),
    ]

    caption = models.TextField(max_length=2000)
    media_url = models.URLField(max_length=500)
    media_type = models.CharField(
        max_length=5,
        choices=[('IMAGE', 'Image'), ('VIDEO', 'Video')],
        default='IMAGE'
    )

    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default='OTHER'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    publisher = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='posts'
    )

    likes_count = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)

    likes = models.ManyToManyField(
        get_user_model(),
        related_name='liked_posts',
        blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Post by {self.publisher.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_comments'
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='user_comments'
    )
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post}"
