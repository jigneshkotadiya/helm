"""helm URL Configuration

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
from django.urls import path, include
from django.conf.urls import handler404, handler500
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('pages.urls')),
    path('engineering/', include('engineering.urls')),

    # all auth 
    path('accounts/', include('allauth.urls')), # new

    # default auth modify
    path('users/', include('users.urls')), # new

    # default auth with django
    # path('users/', include('django.contrib.auth.urls')), # new
]

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns += [
    path('sentry-debug/', trigger_error),
    # ...
]

if settings.DEBUG:
    urlpatterns += [
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    urlpatterns += [
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns