from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import *
from .forms import *
from django.views import generic



# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    neighbourhoods = Neighbourhood.objects.all()
    return render(request, 'home.html',{"neighbourhoods":neighbourhoods,})


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
    return render(request, 'edit_form.html', {"form":form})    



@login_required(login_url='accounts/login/')
def my_profile(request):
    current_user = request.user
    my_hoods = Neighbourhood.objects.filter(user = current_user)
    my_profile = Profile.objects.filter(user = current_user).first
    return render(request, 'profile.html', {"my_hoods": my_hoods, "my_profile":my_profile})


@login_required(login_url='/accounts/login/')
def addhood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')
    else:
        form = NeighbourhoodForm()
    return render(request, 'addhood_form.html', {"form": form}) 

    
def neighbourhood_details(request,neighbourhood_id):
    businesses=Business.objects.filter(neighborhood=neighbourhood_id)
    posts=Post.objects.filter(neighborhood=neighbourhood_id)
    neighbourhood=Neighbourhood.objects.get(pk=neighbourhood_id)
    return render(request,'details.html',{'neighbourhood':neighbourhood,'businesses':businesses,'posts':posts})

@login_required(login_url="/accounts/login/")
def new_business(request,pk):
    current_user = request.user
    neighborhood = get_object_or_404(Neighbourhood,pk=pk)
    if request.method == 'POST':
        business_form = NewBusinessForm(request.POST, request.FILES)
        if business_form.is_valid():
            business = business_form.save(commit=False)
            business.user = current_user
            business.neighborhood=neighborhood
            business.save()
        return redirect('detail', neighbourhood_id=neighborhood.id)
    else:
        business_form = NewBusinessForm()
    return render(request, 'new_business_form.html', {"form": business_form,'neighborhood':neighborhood})

@login_required(login_url="/accounts/login/")
def new_post(request,pk):
    current_user = request.user
    neighborhood = get_object_or_404(Neighbourhood,pk=pk)
    if request.method == 'POST':
        post_form = NewPostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = current_user
            post.neighborhood=neighborhood
            post.save()
        return redirect('detail', neighbourhood_id=neighborhood.id)
    else:
        post_form = NewPostForm()
    return render(request, 'new_post_form.html', {"form": post_form,'neighborhood':neighborhood})


@login_required(login_url='/accounts/login/')
def search_project(request):
    if 'project_name' in request.GET and request.GET["project_name"]:
        search_term = request.GET.get("project_name")
        searched_project = Neighbourhood.search_by_location(search_term)
        message = f"{search_term}"
        return render(request, "search.html",{"message":message,"project": searched_project})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
