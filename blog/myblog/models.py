from django.db import models
from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=5000, null=False, blank=False)
    create_by = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f'{self.title} | {self.author}'
