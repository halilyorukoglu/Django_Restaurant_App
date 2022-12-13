from django.urls import path
from . import views
# http://127.0.0.1:8000/                      => home
# http://127.0.0.1:8000/home                  => home



urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="ana-sayfa"),
    path("/iletisim", views.contact, name="contact"),
    path("/urunler", views.services, name="services"), 
    path("/hakkimizda", views.about, name="about"), 
    


]