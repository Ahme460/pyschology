from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('log/', views.login_view, name='log'),
    path('home/', views.home_view, name='home'),
    path('profile/',views.profile1,name='pro'),
    path('alert/',views.alert,name='alert'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

