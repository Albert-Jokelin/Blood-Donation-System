from django.db import models

choose={
    (0, 'Hospitals'),
    (1, 'Clinics'),
    (2, 'Blood Banks'),
    (3, 'Labs'),
}


class Hospital(models.Model):
    hospital_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=50)  # Classify objects into blood banks, labs, clinics and hospitals
    map_url = models.CharField(max_length=250)
    pincode = models.IntegerField()
    url = models.CharField(max_length=100, default="foobar")
    phone_number = models.IntegerField()
    test_blood = models.BooleanField()
    donate_blood = models.BooleanField()
    x = models.DecimalField(decimal_places=5, max_digits=8, default=0.00000)
    y = models.DecimalField(decimal_places=5, max_digits=8, default=0.00000)
    address = models.CharField(max_length=500, default="LOREM IPSUM")
    image_url = models.CharField(max_length=250, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYlm9vhkUbpK0HCU53rdbzsFSSYNpLDgPPpQ&usqp=CAU")

    def __str__(self):
        return self.name

    def url(self):
        return self.url
