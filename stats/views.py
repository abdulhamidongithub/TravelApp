from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from .models import *

class HomeView(View):
    def get(self, request):
        return render(request, "index.html")

class JourneysView(View):
    def get(self, request):
        form = JourneyForm()
        return render(request, "journeys.html", {"form":form})

    def post(self, request):
        form = JourneyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Journey added successfully!</h1>"
                                "<br>"
                                "<a href='home'>Homepage</a>")
        return redirect("journeys")

class PassengerStatsView(View):
    def get(self, request):
        data = {
            "journeys" : Journey.objects.all()
        }
        return render(request, "passenger_stats.html", data)

class VehicleStatsView(View):
    def get(self, request):
        data = {
            "vehicles":Vehicle.objects.all()
        }
        return render(request, "vehicle_stats.html", data)
