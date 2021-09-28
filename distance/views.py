from django.shortcuts import redirect, render
from geopy.geocoders.base import NONE_RESULT
from .forms import getEndPointForm
import folium
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from django.contrib.gis.geoip2 import GeoIP2


def measure_length(request):
    # or returns one of the objects evaluated left to right
    form = getEndPointForm(request.POST or None)
    geolocator = Nominatim(user_agent="maps")

    map = folium.Map(zoom_start=1)
    map = map._repr_html_()

    if form.is_valid():

        formInstance = form.save(commit=False)
        dest = form.cleaned_data.get('end_point')
        start = form.cleaned_data.get('start_point')
        location = geolocator.geocode(dest)
        start_location = geolocator.geocode(start)

        start_lat = start_location.latitude
        start_long = start_location.longitude
        start_point = (start_lat, start_long)

        end_lat = location.latitude
        end_long = location.longitude
        end_coordinates = (end_lat, end_long)

        trip = geodesic(start_point, end_coordinates).km

        map = folium.Map(location=(end_coordinates), zoom_start=1.5)
        folium.Marker(
            location=(end_coordinates),
            popup=location,
            icon=folium.Icon(color="green"),
        ).add_to(map)
        folium.Marker(
            location=(start_point),
            popup=start_location,
            icon=folium.Icon(color="red"),
        ).add_to(map)
        start_to_end = folium.PolyLine(
            locations=[start_point, end_coordinates], weight=5, color='red')
        map.add_child(start_to_end)
        map = map._repr_html_()

        formInstance.start_point = start_location
        formInstance.end_point = location
        formInstance.trip = trip
        form.save()

    context = {
        'form': form,
        'map': map

    }
    return render(request, 'distance/home.html', context)
