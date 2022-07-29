from django.contrib import admin

# Register your models here.
from .models import sales, watchlist,cates,user

admin.site.register(sales)
admin.site.register(watchlist)
admin.site.register(cates)
admin.site.register(user)
