from django.urls import path
from . import views

urlpatterns = [
    path('<str:article_name>/', views.checkout, name='checkout'),
    path('payment_successful/<str:article_name>/<str:po_ref>/', views.payment_successful, name='payment_successful'),
]