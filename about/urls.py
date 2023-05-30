from django.urls import path
from . import views

# path(endpoint/, function, path-name)
urlpatterns = [
    path('', views.about, name='about-home'),
    path('contact/', views.contact, name='about-contact')
]
