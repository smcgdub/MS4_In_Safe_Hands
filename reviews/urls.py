from django.urls import path
from . import views

urlpatterns = [
    # path('', views.all_products, name=''),
    path('add_review/', views.add_review, name='add_review'),
    path('edit_review/<int:product_id>/', views.edit_review, name='edit_review'),
    path('delete_review/<int:product_id>/', views.delete_review, name='delete_review'),
]