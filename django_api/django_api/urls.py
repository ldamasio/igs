from django.contrib import admin
from django.urls import path, include
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('overview', views.ApiOverview, name='home'),
    path('employee/', include('employee.urls')),
    path('ht/', include('health_check.urls')),
    path('department', views.DepartmentList.as_view(), name='view-all-departments'),
    path('department/create/', views.add_department, name='add-department'),
    path('department/<int:pk>/', views.update_department, name='update-department'),
    path('department/<int:pk>/', views.delete_department, name='delete-department'),
]
