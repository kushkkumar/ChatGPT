from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from gpt import views

urlpatterns = [
    path("", views.GenerationEngineListAPIView.as_view()),
    path("reciever/", views.TextGenerationAPIView.as_view()),
    path('td02/', views.generate_text, name='generate_text'),
]
