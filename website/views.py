
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from django.http import HttpResponseRedirect, Http404
from .models import Posts
from .forms import PostsForm
from django.utils import timezone


def home(request):
    post_list=Posts.objects.active()
    query=request.GET.get("q")
    if query:
        post_list=post_list.filter(
                                       Q(title__icontains=query)|
                                       Q(text__icontains=query)|
                                       Q(user__first_name__icontains=query)|
                                       Q(user__last_name__icontains=query)).distinct()
    paginator = Paginator(post_list, 3) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post = paginator.page(paginator.num_pages)
    title="list views"
    context={
        "title":title,
        "post":post,
        }
    return render(request, "home.html", context)



def about(request):
    return render(request, 'about.html', {})
def contact(request):
    return render(request, 'contact.html', {})
def programs(request):
    return render(request, 'programs.html', {})

def donate(request):
    return render(request, 'donate.html', {})

def team(request):
    return render(request, 'team.html', {})









def create(request):
    if not request.user.is_staff or request.user.is_superuser:
        raise Http404
    form=PostsForm(request.POST or None, request.FILES or None)
    title="Form"
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request, 'post created')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, 'post does not created')
   
    context={
        "title":title,
        'form':form,
        }
    return render(request, "form_news.html", context)


def detail(request, slug=None):
    instance=get_object_or_404(Posts, slug=slug)
    
    context={
        "title":instance.title,
        "instance":instance
        }
    return render(request, "detail_news.html", context)



def update(request, slug=None):
    if not request.user.is_staff or request.user.is_superuser:
        raise Http404
    instance=get_object_or_404(Posts,  slug=slug)
    form=PostsForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request, "messages updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context={
        "form":form,
        "instance":instance
        }
    
    
    
    return render(request, "form_news.html", context)



def delete(request, id=None):
    instance=get_object_or_404(Posts, id=id)
    instance.delete()
    messages.success(request, "messages deleted")
    return redirect("post:list")



