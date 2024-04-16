from django.urls import path
from . import views


urlpatterns = [
    path('blog/',views.blogs,name='blog'),
    path('blog/<int:id>',views.one_blog,name='one_post'),
    path('jops/',views.jobs,name='jobs'),
    path('jop/<int:id>',views.jop,name='jop'),
    path('research/',views.research,name='research'),
    path('books',views.books,name='books'),

    path('down',views.down,name='dowm'),



   
]


