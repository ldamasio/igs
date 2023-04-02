from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeList.as_view(), name='home'),
#    path('create/', views.add_items, name='add-items'),
    path('employee/', views.EmployeeList.as_view(), name='view_all_items'),
#    path('employee/<int:pk>/', views.ViewItem.as_view(), name='view_items'),
#    path('employee/<int:pk>/', views.update_items, name='update-items'),
#    path('employee/<int:pk>/', views.delete_items, name='delete-items'),
]
