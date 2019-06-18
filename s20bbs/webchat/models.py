from django.db import models
from bbs.models import UserProfile

# Create your models here.


class webgroup(models.Model):

    name = models.CharField(max_length=64)
    brief = models.CharField(max_length=255,blank=True,null=True)
    owner = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    admins = models.ManyToManyField(UserProfile,blank=True,related_name="group_admin")
    members = models.ManyToManyField(UserProfile,related_name="group_members")
    max_members = models.IntegerField(default=200)

    def __str__(self):

        return self.name