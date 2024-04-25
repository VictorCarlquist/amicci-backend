from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Retailer(models.Model):
    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Briefing(models.Model):
    name = models.CharField(max_length=100)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    responsible = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    release_date = models.DateField()
    available_date = models.IntegerField()

    def __str__(self):
        return self.name
