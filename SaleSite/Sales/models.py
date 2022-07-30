#from tkinter import CASCADE
from unicodedata import category
from django.db import models

# Create your models here.
class cates(models.Model):
    cate = models.CharField(max_length=40, default=None)

    def __str__(self):
        return self.cate

class sales(models.Model):
    id = models.AutoField(auto_created = True, primary_key = True)
    pic = models.CharField(max_length= 100, default = "A pic would go here")
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    category = models.ForeignKey(cates, on_delete = models.CASCADE, blank = True)
    price = models.IntegerField()

    def __str__(self):
# returns a string representation of the Object
        return f"Item ID: {self.id} -  Description: {self.description}   -   Price: {self.price} $$ -   category: {self.category}"

class watchlist(models.Model):
    name2 = models.ForeignKey(sales, on_delete = models.CASCADE, related_name= "nameOfListing")
    price2 = models.ForeignKey(sales, on_delete = models.CASCADE)

    def __str__(self):
        return f"Article: {self.name} Price: {self.price}"


#class user(models.Model):
 #   count = models.AutoField(auto_created = True, primary_key = True)
  #  username = models.CharField(max_length = 60, name= "username")
   # password = models.CharField(max_length = 50, name ="password")

    #def __str__(self):
     #   return f"count: {self.count}  username:{self.username} "
