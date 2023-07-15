from django.urls import path
from . import views

# path(endpoint/, function, path-name)
urlpatterns = [
    path('', views.home, name='shorts-home'),
    path('my_shorts/', views.my_shorts, name='my_shorts'),
    path('create_shorts/', views.create_shorts, name='create_shorts'),
    path('shorts/<int:short_id>/', views.detailedShorts, name='detailedShorts')
]
