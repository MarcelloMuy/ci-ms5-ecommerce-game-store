"""Imported"""
from django.urls import path
from .import views

urlpatterns = [
    path('<int:product_id>/', views.product_reviews, name='product_reviews'),
    path('reviews_form/<int:product_id>/', views.reviews_form, name='reviews_form'),
    path('<int:product_id>', views.add_review, name='add_review'),
]
