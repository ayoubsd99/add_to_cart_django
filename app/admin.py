from django.contrib import admin

# Register your models here.
from .models import Item,ItemImages

admin.site.register(Item)

admin.site.register(ItemImages)
