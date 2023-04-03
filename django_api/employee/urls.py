from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeList.as_view(), name='view-all-employees'),
    path('create/', views.add_employee, name='add-employee'),
    path('<int:pk>/', views.update_employee, name='update-employee'),
    path('<int:pk>/', views.delete_employee, name='delete-employee'),
]
