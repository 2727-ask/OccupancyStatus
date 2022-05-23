from django.db import models

# Create your models here.



class Hospital(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact1 = models.IntegerField()
    contact2 = models.IntegerField(null=True)
    email = models.EmailField()
    hospitalAddress = models.TextField()
    mapUrl = models.TextField()

    def __str__(self):
        return self.name

class Doctors(models.Model):
    name = models.CharField(max_length=100)
    contact = models.IntegerField()
    email = models.EmailField()
    speciality = models.CharField(max_length=100, null=True)
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.IntegerField()
    email = models.EmailField()
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




