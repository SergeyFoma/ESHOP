from django.contrib import admin

from carts.models import Cart

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product','quantity','session_key','created_timestamp']
