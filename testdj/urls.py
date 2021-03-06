"""testdj URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views import generic
from testproj import views


# from testproj.core import views as core views
admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^summernote/', include('django_summernote.urls')),
    
    re_path(r'^ideas/', views.ideas, name='ideas'),
    re_path(r'^best/', views.best, name='best'),
    re_path(r'^idea/add/', views.add_idea, name='add_idea'),
    re_path(r'^idea/(?P<idea_id>[0-9]+)/edit/', views.edit_idea, name='edit_idea'),
    re_path(r'^idea/(?P<idea_id>[0-9]+)/', views.idea, name='idea'),
    re_path(r'^profile/edit', views.edit_profile, name='edit_profile'),
    re_path(r'^profile/my', views.profile, name='profile'),
    re_path(r'^profile/(?P<username>\w+)/', views.user, name='user'),
    re_path(r'^notifications/', views.notifications, name='notifications'),
    re_path(r'^approvement/', views.approvement, name='approvement'),
    re_path(r'^like/', views.like), # Move to 'hidden_patterns'

    re_path(r'^$', views.home, name='home'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
