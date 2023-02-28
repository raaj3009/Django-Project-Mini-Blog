from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LogInForm, PostForm, ContactForm
from .models import Post, Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
# Create your views here.

# home page
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts':posts})

# about page
def about(request):
    return render(request, 'blog/about.html')

# contact page
def contact(request):
    if request.method == 'POST':
        abc = ContactForm(request.POST)
        if abc.is_valid():
            messages.success(request, 'Successfully Contacted!! We give feedback as soon as possible.')
            abc.save()
        abc = ContactForm()
    else: 
        abc = ContactForm()
    return render(request, 'blog/contact.html', {'contact':abc})

# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user # Profile of author
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'blog/dashboard.html', {'posts':posts,
        'full_name':full_name, 'groups':gps})
    else:
        return HttpResponseRedirect('/login/')

# logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# signup
def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!!! You have become an Author.')
            user=form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form':form})

# login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LogInForm(request=request, data = request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LogInForm()
        return render(request, 'blog/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

# add new post

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
            form = PostForm()
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')


# Edit post
def edit_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)    
        return render(request, 'blog/editpost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')


# delete post
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')


