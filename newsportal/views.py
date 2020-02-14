
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from blog.models import Blog, Category
from django.contrib import messages
from blog.forms import BlogForm

def about(request):
    return render(request, 'about.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        u = request.POST['username']  # request.POST.get("username")
        e = request.POST.get("email")
        p1 = request.POST["password1"]
        p2 = request.POST["password2"]
        if p1 == p2:
            try:
                u = User(username=u, email=e)
                u.set_password(p1)
                u.save()
            except:
                messages.add_message(request, messages.ERROR, "User Not Found")
                return redirect('signup')
            messages.add_message(request, messages.SUCCESS, "Login to continue to your session")
            return redirect('signin')
        else:
            messages.add_message(request, messages.ERROR, "password doesnot match")
            return redirect('signup')


def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        u = request.POST["username"]  # request.POST.get("username")
        p = request.POST["password"]
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, "Password doesnot Match")
            return redirect('signin')


def view_more(request, id):
    # get(id=g_id)

    data=get_object_or_404(Blog,pk=id)
    # data = Blog.objects.get(pk=id)
    data2 = Category.objects.all()
    data3 = Blog.objects.values('id','publish_date','title','image').order_by('publish_date')[:4]
    context = {
        'blog': data,
        'category': data2,
        'blogs':data3
    }

    return render(request, 'view_more.html', context)


def home(request):
    data = Blog.objects.all()
    context = {
        'blog': data
    }
    return render(request, 'home.html', context)

@login_required(login_url='signin')
def dashboard(request):
    return render(request, 'dashboard.html')


def signout(request):
    logout(request)
    return redirect('signin')

def createpost(request):
    form = BlogForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS," Post Created Successfully")
        return redirect('dashboard')
    context = {
        'form':form
    }
    return render(request,'create_post.html',context)

def listpost(request):
    data = Blog.objects.all()
    context = {
        'blog': data
    }
    return render(request,'list_post.html',context)

def editpost(request,id):
    data = Blog.objects.get(pk=id)
    form = BlogForm(request.POST or None,request.FILES or None,instance=data)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, " Post Updated Successfully")
        return redirect('dashboard')
    context = {
        'form':form
    }
    return render(request,'edit_post.html',context)
def deletepost(request,id):
    b = Blog.objects.get(pk=id)
    b.delete()
    messages.add_message(request,messages.SUCCESS,"Post Deleted Successfully")
    return redirect('dashboard')