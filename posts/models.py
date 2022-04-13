from django.db import models
from users.models import User
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    context = models.TextField(max_length=300)
    likes = models.ManyToManyField(
        User, related_name='likes', through='Like')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        "Returns the post title."
        return self.title


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked_date = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['author', 'post'],
                                               name='unique_like')]

    def __str__(self):
        "Returns the like."
        return f'Author:{str(self.author)}, Post:{str(self.post)}, Like Date:{str(self.liked_date)}'
