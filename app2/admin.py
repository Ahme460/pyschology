from django.contrib import admin
from . models import Post,Comment,Jobs,Research,Books_un

admin.site.register(Post)
admin.site.register(Jobs)
admin.site.register(Comment)
admin.site.register(Research)
admin.site.register(Books_un)
# Register your models here.
