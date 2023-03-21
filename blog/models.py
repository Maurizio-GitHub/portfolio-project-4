'''
File hosting the app's data model
'''

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Seen as a PSEUDO (no links) Dimension-Table for status field of Post-Table
class PostStatus(models.Model):

    # Sublclassing and leveraging IntegerChoices
    class Status(models.IntegerChoices):
        DRAFT = 0
        PUBLISHED = 1


# Class-based model for blog posts: blank=False, null=False are the default
class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    excerpt = models.TextField()
    content = models.TextField()
    status = models.IntegerField(choices=Status.choices, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')

    # One-To-Many relationship author-posts with referential integrity
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')

    # Many-To-Many relationship users-likes
    likes = models.ManyToManyField(
        User, related_name='post_likes', blank=True, null=True)

    # Sorting in descending order, based on creation date
    class Meta:
        ordering = ['-created_on']

    # Overriding this default method to return each post by title
    def __str__(self):
        return self.title

    # Simple method to count likes on each post
    def number_of_likes(self):
        return self.likes.count()


# Class-based model for post comments
class Comment(models.Model):

    body = models.TextField()
    commentator = models.CharField(max_length=255)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # One-To-Many relationship post-comments with referential integrity
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')

    # Sorting in ascending order, based on creation date
    class Meta:
        ordering = ['created_on']

    # Overriding this default method to return body and its author
    def __str__(self):
        return f'Comment {self.body} by {self.commentator}'
