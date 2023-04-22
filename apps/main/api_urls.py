from django.urls import path
from main import api_views as view


urlpatterns = [
    path('furniture', view.FurnitureView.as_view()),
]

