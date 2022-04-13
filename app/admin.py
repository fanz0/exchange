from django.contrib import admin
from .models import Profile,Order

class ProfileAdmin(admin.ModelAdmin):
    list_display=('user_profile','btc')

class OrderAdmin(admin.ModelAdmin):
    list_display=('profile','price','quantity')


admin.site.register(Profile,ProfileAdmin)
admin.site.register(Order,OrderAdmin)
