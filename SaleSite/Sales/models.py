from unicodedata import category
from django.db import models

# Create your models here.
class sales(models.Model):
    id = models.AutoField(auto_created = True, primary_key = True)
    pic = models.CharField(max_length= 100, default = "A pic would go here")
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100)
    price = models.IntegerField(max_length = 100)

    def __str__(self):
# returns a string representation of the Object
        return f"{self.id} Description: {self.description} Price: {self.price}"

class watchlist(models.Model):
    name2 = models.ForeignKey(sales, on_delete = models.CASCADE, related_name= "nameOfListing")
    price2 = models.ForeignKey(sales, on_delete = models.CASCADE)

    def __str__(self):
        return f"Article: {self.name} Price: {self.price}"


class user(models.Model):
    count = models.AutoField(auto_created = True, primary_key = True)
    username = models.CharField(max_length = 60)
    password = models.CharField(max_length = 50)

class listingCategories(models.Model):
    prodID = models.ForeignKey(sales.id)
    category = models.CharField(max_length=50)