from django.contrib import admin

from bookshop.models import BookProduct, Producer, AddToCart

admin.site.register(BookProduct)
admin.site.register(Producer)
admin.site.register(AddToCart)
