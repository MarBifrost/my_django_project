from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.category, name='category'),
    path('login/', views.login_views, name='login'),
    path('logout/', views.logout_views, name='logout'),
    # path('products/', views.return_products, name='products_list'),
    # path('categories/', views.return_categories, name='categories_list'),
]
