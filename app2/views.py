from django.shortcuts import render
from . models import Post
from app1.models import Profile
from django.shortcuts import get_object_or_404
from django.core.files.storage import default_storage
from django.conf import settings



# Create your views here.


def blogs(request):
    if request.method=="POST":

        title=request.POST.get('title')
        content=request.POST.get('blog')
        image=request.FILES['image']

        post=Post(title=title,content=content,image=image)
        post.save()
    username = request.session.get('username')
    print(username)
    profile = get_object_or_404(Profile, user__username=username) 
    image_url = None
    if profile.image:
        image_url = settings.MEDIA_URL + str(profile.image)


    posts=Post.objects.all()
    #post_image=posts.image
    #post_title=posts.title
    #post_content=posts.content
    context={
    'image':image_url,
    "posts":posts,
    
    }
    return render(request,'blog.html',context=context)




def one_blog(request,id):


    return render(request,'post.html')