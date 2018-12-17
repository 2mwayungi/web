"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include, url
from django.contrib import admin
from website import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
     
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^programs/$', views.programs, name='programs'),
    url(r'^donate/$', views.donate, name='donate'),
    url(r'^team/$', views.team, name='team'),
    url(r'^blog/', include('posts.urls', namespace="posts")),
   
    url(r'^create/$', views.create, name="create"),
    url(r'^news/(?P<slug>[\w-]+)/$', views.detail, name="detail"),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.update, name="update"),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.delete, name="delete")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
