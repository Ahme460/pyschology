from django.contrib import admin
from . models import Post,Comment,Jobs

admin.site.register(Post)
admin.site.register(Jobs)
admin.site.register(Comment)

# Register your models here.
