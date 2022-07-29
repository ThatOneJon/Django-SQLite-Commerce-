from django.shortcuts import render
from django import forms
from Sales.models import sales, watchlist, cates, user
from django.http import HttpResponse



class create(forms.Form):
    
    yourTitle = forms.CharField(label = "Title", max_length = 100, widget=forms.TextInput(attrs = {'placeholder':'Listing Title'}))
    yourPic = forms.CharField(label = "Picture", max_length = 100, widget=forms.TextInput(attrs = {'placeholder':'Url for Pic'}))
    yourDescription = forms.CharField(label = "Description", max_length = 100, widget=forms.TextInput(attrs = {'placeholder':'Description'}))
    yourPrice = forms.DecimalField(label = "Price", max_digits = 4, widget = forms.NumberInput(attrs = {'placeholder':'Listing Price in $'}))
    yourCategory = forms.ModelChoiceField(queryset = cates.objects.all(), to_field_name = "cate")

class login_user(forms.Form):

    name_user = forms.CharField(label="Username", max_length=30)
    passw_user = forms.CharField(label = "Password", max_length=40, widget = forms.PasswordInput)
    
    class Meta:
        model = user



# Create your views here.
def index(request):
    return render(request,"sales/index.html", {
        "title" : "Welcome to the Store!",
        "listings" : sales.objects.all()
    } )


def createListing(request):
    if request.method == "POST":
        your_title = request.POST["yourTitle"]
        your_price = request.POST["yourPrice"]
        your_description = request.POST["yourDescription"]
        your_pic = request.POST["yourPic"]
        your_category = request.POST["yourCategory"]
    #create it -> autoincrement works -> then add all the values, immediately after!
        new = sales()
        new = sales(pic = your_pic, name = your_title, price = your_price, description = your_description, category = cates.objects.get(cate = your_category))
        new.save()
        return render(request, "sales/index.html")

    
    else:
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

    

def Login(request):
    if request.method == "GET":
        form2 = login_user()
        return render(request,"sales/login.html",{
            "loginForm" : form2
        })

    elif request.method == "POST":
        user_name = request.POST["name_user"]
        password = request.POST["passw_user"]

        if user.objects.get(username = user_name):
            return HttpResponse("Holy cow")
        
        else:
            return HttpResponse(user_name)



    else:
        return HttpResponse("Error 404")