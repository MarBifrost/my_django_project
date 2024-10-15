from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'store'

urlpatterns = [
    path('', views.category, name='category'),
    path('login/', views.login_views, name='login'),
    path('logout/', views.logout_views, name='logout'),
    path('<int:category_id>/products/', views.product_views_by_category, name='product_list'),
    path('product_details/<int:product_id>/', views.product_details, name='product_details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)