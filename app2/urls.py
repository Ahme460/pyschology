from django.urls import path
from . import views


urlpatterns = [
    path('blog/',views.blogs,name='blog'),
    path('blog/<int:id>',views.one_blog,name='one_post')
   
]


