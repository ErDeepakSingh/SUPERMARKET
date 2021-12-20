from django.contrib import admin

from items.models import Category,SubCategory,Item

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Item)
