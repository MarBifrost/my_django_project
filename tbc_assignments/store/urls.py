from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.category, name='category'),
    path('login/', views.login_views, name='login'),
    path('logout/', views.logout_views, name='logout'),
    path('categories/<int:category_id>/', views.product_views_by_category, name='product_list_by_category'),
]
