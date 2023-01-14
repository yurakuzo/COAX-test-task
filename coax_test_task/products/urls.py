from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'order', views.OrderViewSet)

urlpatterns = [
    path('listing/', views.listing, name='listing'),
    path('create-order/', views.create_order, name='create-order'),  # HTML
    path('order/', include(router.urls), name='order'),  # DRF
]
