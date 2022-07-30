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
        return f"Item ID: {self.id} -  Description: {self.description}   -   Price: {self.price} $$ -   category: {self.category} - name: {self.name}"

class bidding_list(models.Model):
    theProduct = models.ForeignKey(sales, on_delete=models.CASCADE)
    bid_now = models.IntegerField(unique = True, default = 1)

    def __str__(self):
        return f"Article: {self.theProduct} bid: {self.bid_now}"


class watchlist(models.Model):
    name_watch = models.CharField(max_length=80, default ="ERROR")
    price_watch = models.IntegerField(default=0)
    bid = models.ForeignKey(bidding_list, to_field='bid_now', on_delete=models.CASCADE)

    def __str__(self):
        return f"Article: {self.name_watch} Price: {self.price_watch} bid: {self.bid}"


#class user(models.Model):
 #   count = models.AutoField(auto_created = True, primary_key = True)
  #  username = models.CharField(max_length = 60, name= "username")
   # password = models.CharField(max_length = 50, name ="password")

    #def __str__(self):
     #   return f"count: {self.count}  username:{self.username} "
