from django.shortcuts import render
from django.views.generic import TemplateView
from helm import settings


class HomePageView(TemplateView):
    template_name = 'home.html'

def AboutView(request):
    context = {
    }
    return render(request, 'pages/about.html', context)


def ContactView(request):
    context = {
        'contact_email': settings.CONTACT_EMAIL
    }
    return render(request, 'pages/contact.html', context)

