from django.contrib import admin
from django.urls import path, include
from stats.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stats/', include("stats.urls")),
    path('', HomeView.as_view(), name="home"),
]
