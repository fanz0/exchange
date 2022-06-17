from django.contrib import admin
from .models import Profile,Order,BuyOffer

class ProfileAdmin(admin.ModelAdmin):
    list_display=('user_profile','btc')

class OrderAdmin(admin.ModelAdmin):
    list_display=('profile','price','quantity','pk')

class BuyOrderAdmin(admin.ModelAdmin):
    list_display=('profile','price','quantity','pk')



admin.site.register(Profile,ProfileAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(BuyOffer,BuyOrderAdmin)
