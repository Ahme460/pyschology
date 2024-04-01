from django.contrib import admin
from .models import CustomUser,Profile
admin.site.register(CustomUser)
# Register your models here.
admin.site.register(Profile)
def save (self, *args, **kwargs):
    """saving to DB disabled"""
    pass