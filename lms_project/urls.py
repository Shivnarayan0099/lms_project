"""
URL configuration for lms_project project.

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
from lms.views import home, login_view, dashboard, logout_view
from lms.views import courses
from lms.views import enroll
from lms.views import course_detail
from lms.views import my_courses

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home),
    path('login/',login_view),
    path('dashboard/', dashboard),
    path('logout/', logout_view),
    path('courses/', courses),
    path('enroll/<int:course_id>/', enroll),
    path('courses/<int:course_id>/', course_detail),
    path('my-courses/', my_courses),
]
