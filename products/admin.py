from django.contrib import admin
from .models import Product, Client, Seller, Video
# Register your models here.

# Customize the admin panel
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'active']
    list_display_links = ['name', 'price']
    list_editable = ['active']
    list_filter = ['category']
    search_fields = ['name', 'price', 'category']
    # fields = ['name', 'price'] -> to choose what to show in the details about the object


admin.site.register(Product, ProductAdmin)
admin.site.register(Video)
admin.site.register(Client)
admin.site.register(Seller)
admin.site.site_header = 'Admin Panel'
admin.site.site_title = 'Admin Panel'

