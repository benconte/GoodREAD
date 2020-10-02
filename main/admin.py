from django.contrib import admin
from .models import Books, BuyBook, Comments
# Register your models here.
admin.site.register(Books)
admin.site.register(BuyBook)
admin.site.register(Comments)
