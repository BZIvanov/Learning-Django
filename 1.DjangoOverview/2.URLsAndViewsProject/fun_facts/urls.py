"""
URL configuration for fun_facts project.

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
from django.urls import path, include

# include our apps to the project so Django knows for their existence
urlpatterns = [
    path("admin/", admin.site.urls),
    path("math-facts/", include("math_facts.urls")),
    path("seasonal-facts/", include("seasonal_facts.urls")),
    path("nature-facts/", include("nature_facts.urls")),
]
