from django.contrib import admin
from django.urls import path, include
from challenges import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('challenge/', include('challenges.urls')),
    path('', views.Home, name="home"),
    path('/success', views.Success, name="success"),
]
