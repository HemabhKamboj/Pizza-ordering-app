from django.contrib import admin

from django.contrib.auth.models import User
from .models import PizzaTopping, SubExtra, MenuItem, OrderItem, Order
# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

class OrderItemAdmin(admin.ModelAdmin):
    filter_horizontal = ("toppings", "extras",)

admin.site.register(PizzaTopping)
admin.site.register(SubExtra)
admin.site.register(MenuItem)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
