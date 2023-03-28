"""atcadminpanel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ATCadmin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_login', views.admin_login_view, name='admin_login'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('admin_add', views.add, name='add'),
    path('admin_edit', views.edit, name='edit'),
    path('admin_update/<str:id>', views.update, name='update'),
    path('admin_delete/<str:id>', views.delete, name='delete'),
    path('admin_logout', views.admin_logout_view, name='admin_logout'),
]
