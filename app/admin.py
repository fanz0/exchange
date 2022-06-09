from django.contrib import admin
from .models import Profile,Order,SellOrder

class ProfileAdmin(admin.ModelAdmin):
    list_display=('user_profile','btc')

class OrderAdmin(admin.ModelAdmin):
    list_display=('profile','price','quantity')

class SellOrderAdmin(admin.ModelAdmin):
    list_display=('buyer_profile','buyer_price','buyer_quantity')


admin.site.register(Profile,ProfileAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(SellOrder,SellOrderAdmin)