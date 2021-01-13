from django.db import models


class Bank(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.id}-{self.name}'


class Branches(models.Model):
    ifsc = models.CharField(max_length=11, primary_key=True)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch = models.CharField(max_length=75, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.ifsc}-{self.bank_id}-{self.branch}'
