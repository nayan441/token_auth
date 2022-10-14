
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date

class User(AbstractUser):
  username = models.CharField(max_length = 50, null = True, unique = True)
  email = models.EmailField(unique = True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []# will ask when we create super user
  def __str__(self):
      return "{}".format(self.email)


class Org(models.Model):
    name = models.CharField(max_length=50, blank = True, null = True, unique = True)
    created_by = models.ForeignKey(User, on_delete= models.CASCADE,blank = True, null = True,)

class Channel(models.Model):
    name = models.CharField(max_length=50, blank = True, null = True, unique = True)
    org = models.ForeignKey(Org,on_delete= models.CASCADE, blank = True, null = True,)
    created_by = models.ForeignKey(User,on_delete= models.CASCADE, blank = True, null = True,)