from django.contrib import admin

# Register your models here.
from .models import sales, watchlist

admin.site.register(sales)
admin.site.register(watchlist)