from django.http import response
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from news.forms import NewsForm
from news.models import Post

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.utils.translation import gettext as _

@login_required(login_url='login')
def homePage(request):
    context = {}
    object_list = Post.objects.all()
    object_list = object_list.order_by('-created_at')
    paginator = Paginator(object_list, 4)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context['posts'] = posts

    return render(request, 'newsdata.html', context)

def post_detail(request, post):
    posts = get_object_or_404(Post, slug = post)
    return render(request, 'detail.html', {'posts': posts})


def logoutUser(request):
    logout(request)
    messages.info(request, 'User logged out!')
    return redirect('login')
    
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Unknown Account, Please re-enter!')
    
    return render(request, 'login.html', {})

def regPage(request):
    form = UserCreationForm()
    context = {}
    if request.method == 'POST':
        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')
    context['form'] = form
    return render(request, 'register.html', context)

def add(request):
    context = {}
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                pass
    else:
        form = NewsForm()
    context['form'] = form
    return render(request, 'add.html', context)

def edit(request, id):
    context = {}
    post = Post.objects.get(id=id)
    context['post'] = post
    return render(request,'edit.html', context)  

def update(request, id):  
    context = {}
    post = Post.objects.get(id=id)  
    form = NewsForm(request.POST, instance = post)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    context['post'] = post
    return render(request, 'edit.html', context)  

def destroy(request, id):  
    post = Post.objects.get(id=id)  
    post.delete()  
    return redirect("/")  
            