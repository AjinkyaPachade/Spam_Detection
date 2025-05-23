
from django.contrib import admin
from .models import PhoneNumber

@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'is_spam', 'owner_name', 'image')  # Add 'image' here
    fields = ('number', 'is_spam', 'owner_name', 'image')  # Add 'image' here
