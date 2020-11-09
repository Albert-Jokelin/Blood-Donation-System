from django.db import models


class BloodBank(models.Model):
    name = models.CharField(max_length=250)
    map_url = models.CharField(max_length=250)
    pincode = models.IntegerField()
    phone_number = models.IntegerField()
    donate_blood = models.BooleanField()

    def __str__(self):
        return self.name + ' ' + self.phone_number + '  ' + self.pincode


class Hospital(models.Model):
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=50)  # Classify objects into labs, clinics and hospitals
    map_url = models.CharField(max_length=250)
    pincode = models.IntegerField()
    phone_number = models.IntegerField()
    test_blood = models.BooleanField()
    donate_blood = models.BooleanField()

    def __str__(self):
        return self.name + ' ' + self.phone_number + '  ' + self.pincode
