from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('overview', views.ApiOverview, name='home'),
    path('employee/', include('employee.urls')),
    path('ht/', include('health_check.urls')),
]
