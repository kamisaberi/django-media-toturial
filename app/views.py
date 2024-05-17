from django.shortcuts import render , redirect
from django.core.files.storage import FileSystemStorage
import random
from .models import Post

# Create your views here.


def form(request) :
    posts = list(Post.objects.all())
    psts=[]
    # for post in posts:
    #     psts.append({"id" :post.id , "title" :post.title , "content":post.content , "profile" : str(post.profile)   })
        # print(post.profile)
    return render(request , "form.html" , {"posts" : posts} )

def save(request) :
    if request.method == 'POST' and request.FILES['profile']:
        myfile = request.FILES['profile']
        fs = FileSystemStorage()
        name = random.randint(1,1000000)
        filename = fs.save(str(name) + ".jpg", myfile)
        uploaded_file_url = fs.url(filename)
        Post.objects.create(
            title = request.POST["title"],
            content = request.POST["content"],
            profile  = uploaded_file_url
            )

    return redirect("/app/form")
    



def page(request) :
    pass
