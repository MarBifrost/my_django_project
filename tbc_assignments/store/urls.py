from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.store, name='store'),
    path('login/', views.login_views, name='login'),
    path('logout/', views.logout_views, name='logout'),
]
