from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import CustomUser ,Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.files.storage import default_storage
from django.conf import settings
import os

def home_view(request):
    username = request.session.get('username')
    user = CustomUser.objects.get(username=username)  # Retrieve the user object using the username
    print(username)

    profiles = Profile.objects.filter(user=user)  # Filter profiles by the user object

    image_url = None  # Initialize image_url to None
    if profiles.exists():  # Check if any profiles exist for the user
        profile = profiles.first()  # Get the first profile object
        if profile.image:  # Check if the profile has an image
            image_url = settings.MEDIA_URL + str(profile.image)

    context = {
        "image": image_url
    }
    return render(request, 'home.html', context=context)

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        type_ = request.POST.get('category')
        request.session['username'] = username

        if username and email and password and type_:
            existing_users = CustomUser.objects.filter(Q(username=username) | Q(email=email))
            
            if existing_users:
                messages.error(request, 'email incorrect')
            else:
                user = CustomUser(username=username, email=email, role=type_)
                user.set_password(password)
                user.save()
                return redirect('log')
        else:
            messages.error(request, 'enter all data')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['username'] = username
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            return redirect('home')
        else:
            messages.error(request, 'user not found')

    return render(request, 'login.html')

def profile1(request):
     
    username = request.session.get('username')
    print(username)
    profile = get_object_or_404(Profile, user__username=username)  # الحصول على البروفايل المرتبط بالمستخدم
    email = profile.user.email
    exper=profile.experience
    cer=profile.certificates
    about_me=profile.about_me
   # age = profile.user.age
    image_url = None
    if profile.image:
        image_url = settings.MEDIA_URL + str(profile.image)
    

    context={

'username': username,
 'email': email,
'image_url': image_url,
'exper':exper,
'cer':cer,
'about':about_me




    }



    return render(request, 'acount.html',context=context )
   

def alert(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user__username=request.session.get('username'))
        profile_ex = profile.experience
        profile_cer = profile.certificates
        profile_about_me=profile.about_me

        if 'image' in request.FILES:
            # Delete the old image if it exists
            if profile.image:
                file_path = os.path.join(settings.MEDIA_ROOT, str(profile.image))
                if default_storage.exists(file_path):
                    default_storage.delete(file_path)
            profile.image = request.FILES['image']

        profile.about_me = request.POST.get('about_me')
        profile.experience = request.POST.get('experience')
        profile.certificates = request.POST.get('certificates')

        def constant(value, equal):
            length = len(value)
            if length <= 0:
                value = equal
            return value

        # Update experience and certificates using the constant function
        profile.experience = constant(request.POST.get('experience'), profile_ex)
        profile.certificates = constant(request.POST.get('certificates'), profile_cer)
        profile.about_me = constant(request.POST.get('about_me'),profile_about_me )
        profile.save()


    return render(request, 'alert.html')