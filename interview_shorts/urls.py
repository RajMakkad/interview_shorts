"""
URL configuration for interview_shorts project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from users import views as user_view
from django.conf import settings
from django.conf.urls.static import static

# path(endpoint/, function, path-name)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shorts.urls')),
    path('about/', include('about.urls')),
    path('user/register/', user_view.register, name='register'),
    path('user/login/', user_view.login, name='login'),
    path('user/logout/', user_view.logout, name='logout'),
    path('user/profile/', user_view.profile, name='profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)