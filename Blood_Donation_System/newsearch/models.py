from django.db import models


class Hospital(models.Model):
    hospital_id = models.IntegerField()
    url = models.CharField(max_length=1000)
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=50)  # Classify objects into blood banks, labs, clinics and hospitals
    map_url = models.CharField(max_length=250)
    pincode = models.IntegerField()
    phone_number = models.IntegerField()
    test_blood = models.BooleanField()
    donate_blood = models.BooleanField()

    def __str__(self):
        return self.name + ' ' + str(self.phone_number )+ '  ' + str(self.pincode)
