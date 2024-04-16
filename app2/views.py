from django.shortcuts import render
from . models import Post , Comment,Jobs,Research,Books_un
from app1.models import Profile,CustomUser
from django.shortcuts import get_object_or_404
from django.core.files.storage import default_storage
from django.conf import settings
from reportlab.pdfgen import canvas

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
  
    size_in_bytes = sys.getsizeof(jobs[0])
    print("size: "+str(size_in_bytes))


    lista = [[], [], [], [],[],[]]
    jobs = list(jobs)  # Assuming `jobs` is a list of objects
    ahmed = 0
    length = len(jobs)  # Assuming jobs has elements
    print(sys.getsizeof(jobs))
    for job in range(length):
        lista[0].append(jobs[0].title)
        lista[1].append(jobs[0].descrbtion)  # Typo? Should it be `description`?
        lista[2].append(jobs[0].place)
        lista[3].append(jobs[0].skills)
        lista[4].append(jobs[0].image)
        lista[5].append(jobs[0].job_id)


        


        jobs.pop(0)
        ahmed += 1
    
    del jobs
    
    

   


    
    
    print(sys.getsizeof(("size: "+str(lista))))
    combined_list = zip(lista[0], lista[1], lista[2], lista[3],lista[4],lista[5])
    del lista
    

    combined_list=list(combined_list)    
    reversed_list=combined_list[-1:None:-1]
    combined_list=None
    print(jobss,combined_list)
    

    print(type(reversed_list))
    context={
       'image':image_url,
     
          'combined_list': combined_list,
          
    
        'list':reversed_list,
    
    }
    


    
    




  


    return render(request,'jobs.html' ,context=context)





def jop(request, id):
    print(id)
    _jop = Jobs.objects.get(job_id=id)


    skills = _jop.skills.splitlines() 

    context = {
            'jop': _jop,
            'skills': skills,
        }

 





    return render(request,'jop.html',context=context)




def research(request):

    research=Research.objects.all()

    conntext={
        'research':research
    }


    return render(request,'reserch.html',context=conntext)
from PyPDF2 import PdfReader, PdfWriter
from django.http import HttpResponse

def books(request):
    books = Books_un.objects.all()

 
   

    # تحقق من وجود كتب
    if books.exists():
        book = books.first() 

        # إنشاء كائن Convert وتنفيذ عملية التحويل
       
     

    context = {
        'books': books
    }

    return render(request, 'books.html', context=context)
from .con_pd import Convert


def down(request):
    username = request.session.get('username')
    user = CustomUser.objects.get(username=username)
    user = str(user)
    books = Books_un.objects.all()

    # تحقق من وجود كتب
    if books.exists():
        book = books.first()

        # إنشاء كائن Convert وتنفيذ عملية التحويل
        obj = Convert(user, book.book_pdf.path)
        print(book.book_pdf.path)

        # استدعاء دالة convert من الكائن واستخدام الاستجابة كاستجابة للعميل
        response = obj.convert()
        print("done convert")

        return response

