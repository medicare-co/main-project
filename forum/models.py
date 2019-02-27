from django.db import models
from home.models import User

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=100)
    content = models.TextField(max_length=8000)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} | {}".format(self.question, self.likes)

class Comment(models.Model):
    post = models.ForeignKey(Question, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=3000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} ON {}".format(self.user, self.post)