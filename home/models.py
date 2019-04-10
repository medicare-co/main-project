from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.URLField(default='')
    address = models.CharField(default='', max_length=200)
    phone = models.CharField(default='', max_length=10)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


class Order(models.Model):
    name = models.CharField(max_length=100)
    contents = models.TextField(max_length=2000)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Name: {} User: {}".format(self.name, self.user)
