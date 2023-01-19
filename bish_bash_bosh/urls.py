from django.contrib import admin
from django.urls import path
from challenges import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('challenge/', views.Challenge, name="challenge")
]
