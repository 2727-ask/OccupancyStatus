from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.IntegerField()
    address = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Hospital(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact1 = models.IntegerField(null=True)
    contact2 = models.IntegerField(null=False)
    email = models.EmailField(null=True)
    display_photo = models.ImageField(upload_to='media',null=True)
    hospitalAddress = models.TextField()
    mapUrl = models.TextField()
    def __str__(self):
        return self.name


class Doctors(models.Model):
    name = models.CharField(max_length=100)
    contact = models.IntegerField()
    email = models.EmailField(null=True)
    speciality = models.CharField(max_length=100, null=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media", null=True)

    def __str__(self):
        return self.name


class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True)
    contact = models.IntegerField(null=True)
    email = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='media',null=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=100)
    total = models.IntegerField()
    remaining = models.IntegerField()
    last_updated = models.DateTimeField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField()
    status = models.BooleanField(default=False)
    service_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
