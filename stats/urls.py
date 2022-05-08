from django.urls import path
from .views import *

urlpatterns = [
    path('add_journey/', JourneysView.as_view(), name="add-journey"),
    path('vehicles/', VehicleStatsView.as_view(), name="vehicles"),
    path('passengers/', PassengerStatsView.as_view(), name="passengers"),
]
