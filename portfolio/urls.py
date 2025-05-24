
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

# URLs do app portfolio
app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('send-contact/', views.send_contact_email, name='send_contact'),
    path('project/<int:project_id>/', views.get_project_detail, name='project_detail'),
]