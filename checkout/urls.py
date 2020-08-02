from django.urls import path
from . import views

urlpatterns = [
    path('<str:article_name>/', views.checkout, name='checkout'),
    path('payment_successful/<str:po_ref>/', views.checkout, name='payment_successful'),
]