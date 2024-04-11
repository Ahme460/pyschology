from django.shortcuts import render
from . models import Post , Comment,Jobs
from app1.models import Profile,CustomUser
from django.shortcuts import get_object_or_404
from django.core.files.storage import default_storage
from django.conf import settings



# Create your views here.
def blogs(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('blog')

        # Get the image from the request
        if 'image' in request.FILES:
            image = request.FILES['image']
            print('exist')
        else:
            image = None
            print(image)
        username = request.session.get('username')
        profile = get_object_or_404(Profile, user__username=username)

        # Ensure the profile exists before creating the post
        if profile:
            custom_user_instance = profile.user
            # Create a Post instance with the provided data
            post = Post(title=title, content=content, author=custom_user_instance)

            if image:
                post.image = image  # Assign the image to the 'image' field

            post.save()
            # Handle further operations
        else:
            # Handle the case where the profile is not found
            pass

    username = request.session.get('username')
    print(username)
    profile = get_object_or_404(Profile, user__username=username)
    image_url = None
    if profile.image:
        image_url = settings.MEDIA_URL + str(profile.image)
    posts = Post.objects.all()
    context = {
        'image': image_url,
        'posts': posts,
    }
    return render(request, 'blog.html', context=context)

def one_blog(request, id):
    username = request.session.get('username')
    author = CustomUser.objects.get(username=username)
    profile=Profile.objects.get(user=author)

    post = Post.objects.get(id=id)
    print(post)

    comment = ''

    if request.method == 'POST':
        comment = request.POST.get('comment')

    if len(comment) >= 1:
        comm = Comment(content=comment, post=post, author=author)
        comm.save()
    comments=list

    comments = Comment.objects.filter(post=post)
    print("type cooments is : "+ str(type(comments)))

    


    context = {
        "post": post,
        "comments": comments,
        'profile':profile
    }

    return render(request, 'post.html', context=context)


def jobs(request):
    import sys

    user=request.session.get('username')
    user1=Profile.objects.get(username=user)
    if user1.image:
        image_url = settings.MEDIA_URL + str(user1.image)
    
    jobss=[]
    jobs=Jobs.objects.all()
    jobss=list(jobs)
    size_in_bytes = sys.getsizeof(jobs[0])
    print("size: "+str(size_in_bytes))
    lista=[[],[],[],[]]
    for i in jobs:
        lista[0].append(i.title)
        lista[1].append(i.descrbtion)
        lista[2].append(i.place)
        lista[3].append(i.skills)
    ahmed=0
    for i in range(len(lista[0])):
        ahmed+=1


    print("ahmed is equl: "+str(ahmed))

    
    print(lista)
    print(sys.getsizeof(("size: "+str(lista))))

    
    context={
        'image':image_url,
        'list2':lista[2],
        
    
        'list':lista,
    
    }
    


    
    




  


    return render(request,'jobs.html' ,context=context)