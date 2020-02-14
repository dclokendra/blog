"""newsportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.home),
                  path('about/', views.about),
                  path('post/create', views.createpost, name='createpost'),
                  path('post/<int:id>/edit', views.editpost, name='editpost'),
                  path('post/<int:id>/delete', views.deletepost, name='deletepost'),
                  path('post/list', views.listpost, name='listpost'),
                  path('blog/<int:id>', views.view_more, name='view_more'),
                  path('signup/', views.signup, name='signup'),
                  path('signin/', views.signin, name='signin'),
                  path('signout/', views.signout, name='signout'),
                  path('dashboard/', views.dashboard, name='dashboard'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
