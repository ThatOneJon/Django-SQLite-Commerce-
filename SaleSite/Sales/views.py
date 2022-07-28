from django.shortcuts import render
from django import forms
from Sales.models import sales, watchlist, cates
from django.http import HttpResponse



class create(forms.Form):
    yourTitle = forms.CharField(label = "Title", max_length = 100, widget=forms.TextInput(attrs = {'placeholder':'Listing Title'}))
    yourPic = forms.CharField(label = "Picture", max_length = 100, widget=forms.TextInput(attrs = {'placeholder':'Url for Pic'}))
    yourDescription = forms.CharField(label = "Description", max_length = 100, widget=forms.TextInput(attrs = {'placeholder':'Description'}))
    yourPrice = forms.DecimalField(label = "Price", max_digits = 4, widget = forms.NumberInput(attrs = {'placeholder':'Listing Price in $'}))



# Create your views here.
def index(request):
    return render(request,"sales/index.html", {
        "title" : "Welcome to the Store!",
        "listings" : sales.objects.all()
    } )



def createListing(request):
    return render(request, "sales/createListing.html", {
        "title" : "Create Listing",
        "the_form" : create()
    })


def listingSite(request, Sid):
    thisListing = sales.objects.get(id=Sid)
    thisListing_name = thisListing.name
    thisListing_pic = thisListing.pic

    return render(request, "sales/listing.html", {
        "this_listing" : thisListing, 
        "title" : thisListing_name,
        "pic" : thisListing_pic
    })

def cat(request):
    return render(request, "sales/category.html", {
        "Categories_all":cates.objects.all(),
        "title":"Category Listing"
    })

def catDetail(request, categ):
    all=sales.objects.filter(category=cates.objects.get(cate=categ))
    if all:
        return render(request, "sales/catDetail.html", {
            "theListings":all,
            "title":categ

        })
    else:
        return render(request,"sales/catDetail.html", {
            "title":"Nothing here"
        })


