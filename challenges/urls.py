from django.urls import path
from . import views

urlpatterns = [
    path('<int:challenge_id>/', views.Challenge, name='challenge'),
]