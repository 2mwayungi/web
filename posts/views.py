from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from .models import Post
from django.db.models import Q
from django.utils import timezone
from .forms import PostForm

def list(request):
    today=timezone.now().date()
    queryset_list=Post.objects.active()
    if request.user.is_staff or request.user.is_superuser:
         queryset_list=Post.objects.all()
    query=request.GET.get('q')
    if query:
        queryset_list=queryset_list.filter(Q(title__icontains=query)|
                                           Q(content__icontains=query)|
                                           Q(user__first_name__icontains=query)|
                                           Q(user__last_name__icontains=query)
                                           ).distinct()
        
         
    paginator = Paginator(queryset_list, 6) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset= paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
       queryset = paginator.page(paginator.num_pages)

    title="Blog"
    context={
        "today":today,
        "title":title,
        'object_list':queryset,
        }
    
    return render(request, 'list.html', context)






def detail(request, slug=None):

    instance=get_object_or_404(Post, slug=slug)
    if instance.publish > timezone.now() or instance.draft:
       if not request.user.is_staff or not request.user.is_superuser:
         raise Http404
  
    context={
        'instance':instance,
        'title':instance.title,
        }
    return render(request, 'details.html', context)

def create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form=PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        messages.success(request, 'successfuly created')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "not successfully created")
    context={
        'form':form,
        }
    
    return render(request, 'forms.html', context)

def update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance=get_object_or_404(Post, slug=slug)
    form=PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request, 'successfully updated')
        return HttpResponseRedirect(instance.get_absolute_url())

    context={
        'form':form,
        'instance':instance,
        }
    
    return render(request, 'forms.html', context)
def delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance=get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, 'successfully deleted')
    
    return redirect('posts:list')
