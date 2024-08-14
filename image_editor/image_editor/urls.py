"""
URL configuration for image_editor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from editor import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # Root URL pattern
    path('upload/', views.upload_image, name='upload_image'),
    path('newupload/', views.newupload, name='newupload'),
    path('save_image/', views.save_image, name='save_image'),  # Add this line
    path('login/', views.user_login, name='login'),  # Add this line
    path('logout/', views.user_logout, name='logout'),  # Add this line
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
