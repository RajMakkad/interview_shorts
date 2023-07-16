from django.urls import path
from . import views

# path(endpoint/, function, path-name)
urlpatterns = [
    path('', views.home, name='shorts-home'),
    path('my_shorts/', views.my_shorts, name='my_shorts'),
    path('create_shorts/', views.create_shorts, name='create_shorts'),
    path('delet_shorts/<int:short_id>/', views.delete_shorts, name='delete_shorts'),
    path('update_shorts/<int:short_id>/', views.update_shorts, name='update_shorts'),
    path('shorts/<int:short_id>/', views.detailedShorts, name='detailedShorts')
]
