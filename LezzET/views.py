from django.shortcuts import render
from LezzET.models import LezzET 



# Create your views here.
def home(request):
    context = {
        "products": LezzET.objects.filter(is_active=True, is_home=True),        
    }
    return render(request, "LezzET/home.html", context)


def contact(request):
    context = {
        "contact": LezzET.objects.filter(is_active=True, is_home=True),        
    }
    return render(request, "LezzET/contact.html", context)

def services(request):
    context = {
        "services": LezzET.objects.filter(is_active=True, is_home=True),       
    }
    return render(request, "LezzET/services.html", context)

def about(request):
    context = {
        "about": LezzET.objects.filter(is_active=True, is_home=True),        
    }
    return render(request, "LezzET/about.html", context)


