from django.urls import path
from .views import landing, about, login, custom_login_view
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns =[
    #ke halaman home
    path('', landing, name='landing'),

    #ke halaman about
    path('about/', about, name='about'),

    #form login
    path('login/', custom_login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

     # halaman services
    path('services/', TemplateView.as_view(template_name='services.html'), name='services'),
 
]