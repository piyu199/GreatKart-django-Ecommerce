from django.contrib import admin
from .models import Cart,CartItem

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display=('carts_id','created_date')



class CartItemAdmin(admin.ModelAdmin):
    list_display=('product','cart','quantity','is_active')


admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem,CartItemAdmin)