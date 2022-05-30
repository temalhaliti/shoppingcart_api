from django.urls import path
from .views import ProductViews

urlpatterns = [
    path('product/', ProductViews.as_view()),
    path('product/<int:id>', ProductViews.as_view())
]