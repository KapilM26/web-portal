from django.db import models
from os.path import join


# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=200)
    exp = models.CharField(max_length=20, null=True, blank=True)
    domain = models.CharField(max_length=1000,)
    designation = models.CharField(max_length=1000, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    biodata = models.FileField(null=True, blank=True)
    #file_url=models.CharField(max_length=200)

    def __str__(self):
        return self.name + '-' + self.domain

    def create(self, **kwargs):
        self.name = kwargs['name']
        self.exp = kwargs['exp']
        self.domain = kwargs['domain']
        self.designation = kwargs['designation']
        self.email = kwargs['email']
        self.phone = kwargs['phone']



class TempProfileAdd(models.Model):
    name = models.CharField(max_length=200)
    exp = models.CharField(max_length=20, null=True, blank=True)
    domain = models.CharField(max_length=1000)
    designation = models.CharField(max_length=1000, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    biodata = models.FileField(null=True, blank=True)
    #file_url=models.CharField(max_length=200)

    def __str__(self):
        return self.name + '-' + self.domain

    def create(self, **kwargs):
        self.name = kwargs['name']
        self.exp = kwargs['exp']
        self.domain = kwargs['domain']
        self.designation = kwargs['designation']
        self.email = kwargs['email']
        self.phone = kwargs['phone']


class TempProfileEdit(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    exp = models.CharField(max_length=20, null=True, blank=True)
    domain = models.CharField(max_length=1000)
    designation = models.CharField(max_length=1000, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    biodata = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name + '-' + self.domain

class TempProfileDelete(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.name + '-' + self.profile.domain

    def create(self, obj):
        self.profile = obj

class Log(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
