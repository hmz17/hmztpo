from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    father_name = models.CharField(max_length=30, blank=True, null=True)
    mother_name = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(auto_now=False, blank=True, null=True)
    contact1 = models.DecimalField(decimal_places=0,max_digits=15, blank=True, null=True)
    contact2 = models.DecimalField(decimal_places=0,max_digits=15, blank=True, null=True)
    contact3 = models.DecimalField(decimal_places=0,max_digits=15, blank=True, null=True)
    permanent_address = models.CharField(max_length=100, blank=True, null=True)
    residential_address = models.CharField(max_length=100, blank=True, null=True)
    resume_file = models.FileField(upload_to='doc', blank=True, null=True)

    def __str__(self):
        return self.user.first_name +' '+  self.user.last_name



User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class Resume(models.Model):
    user = models.OneToOneField(User,unique=True)
    file = models.FileField(upload_to='doc')

    def __str__(self):
        return self.user.first_name +' '+  self.user.last_name
