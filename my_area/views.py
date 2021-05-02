from django.shortcuts import render
from .forms import *
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import *
from django.views import generic

@login_required(login_url='/accounts/login/')
def home(request):
    mylocs = Myloc.objects.all()
    return render(request, 'home.html',{"mylocs":mylocs,})

@login_required(login_url='accounts/login/')
def add_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(id = current_user.id)
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            caption = form.save(commit=False)
            caption.user = current_user
            caption.save()
            return redirect('myprofile')
    else:
        form = NewProfileForm()
    return render(request, 'edit.html', {"form":form})    

@login_required(login_url='accounts/login/')
def my_profile(request):
    current_user = request.user
    my_my_area = Myloc.objects.filter(user = current_user)
    my_profile = Profile.objects.filter(user = current_user).first
    return render(request, 'profile.html', {"my_my_areas": my_my_areas, "my_profile":my_profile})

@login_required(login_url='/accounts/login/')
def addmy_area(request):
    current_user = request.user
    if request.method == 'POST':
        form = MylocForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')
    else:
        form = MylocForm()
    return render(request, 'addmy_area.html', {"form": form}) 
    
def myloc_details(request,myloc_id):
    activities=Activity.objects.filter(myloc=myloc_id)
    posts=Post.objects.filter(myloc=myloc_id)
    myloc=Myloc.objects.get(pk=myloc_id)
    return render(request,'details.html',{'myloc':myloc,'activities':activities,'posts':posts})

@login_required(login_url="/accounts/login/")
def new_activity(request,pk):
    current_user = request.user
    myloc = get_object_or_404(Myloc,pk=pk)
    if request.method == 'POST':
        activity_form = NewActivityForm(request.POST, request.FILES)
        if activity_form.is_valid():
            activity = activity_form.save(commit=False)
            activity.user = current_user
            activity.myloc=myloc
            activity.save()
        return redirect('detail', myloc_id=myloc.id)
    else:
        activity_form = NewActivityForm()
    return render(request, 'new_activity.html', {"form": activity_form,'myloc':myloc})

@login_required(login_url="/accounts/login/")
def new_post(request,pk):
    current_user = request.user
    myloc = get_object_or_404(Myloc,pk=pk)
    if request.method == 'POST':
        post_form = NewPostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = current_user
            post.myloc=myloc
            post.save()
        return redirect('detail', myloc_id=myloc.id)
    else:
        post_form = NewPostForm()
    return render(request, 'new_post.html', {"form": post_form,'myloc':myloc})


@login_required(login_url='/accounts/login/')
def search_project(request):
    if 'project_name' in request.GET and request.GET["project_name"]:
        search_term = request.GET.get("project_name")
        searched_project = Myloc.search_by_location(search_term)
        message = f"{search_term}"
        return render(request, "search.html",{"message":message,"project": searched_project})
    else:
        message = "No search history"
        return render(request, 'search.html',{"message":message})

