from django.urls import path
from . import views


app_name = 'order'


urlpatterns = [
    path('', views.order, name='order'),
    path('Payment/', views.payment_success, name='payment_success'),

]
