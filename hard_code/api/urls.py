from django.urls import include, path
from rest_framework import routers

from api import views


app_name = "api"


urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('user-product-access/', views.UserProductAccessList.as_view(), name='user-product-access-list'),
    path('lessons/', views.LessonList.as_view(), name='lesson-list'),
    path('lesson-views/', views.LessonViewList.as_view(), name='lesson-view-list'),
    path('lessons/<int:user_id>/', views.UserLessonsList.as_view(), name='user-lessons-list'),
    path('product/<int:product_id>/lessons/', views.ProductLessonsList.as_view(), name='product-lessons-list'),
    path('product-stats/', views.ProductStats.as_view(), name='product-stats'),
]