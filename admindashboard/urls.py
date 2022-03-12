from django.urls import path

from admindashboard import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
]