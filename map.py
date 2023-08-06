import folium
from geopy.geocoders import Nominatim

# List of people with their addresses
people = {
    'Person 1': 'Sydney, NSW, 2000, Australia',
    'Person 2': 'Seattle, Bellevue, WA, 98008, USA',
}

# Initialize the geolocator
geolocator = Nominatim(user_agent="map_location_app")

# Create a folium map centered on the first person's location
first_person_address = list(people.values())[0]
first_person_location = geolocator.geocode(first_person_address)
map_location = folium.Map(location=[first_person_location.latitude, first_person_location.longitude], zoom_start=10)

# Add markers for each person's location
for person, address in people.items():
    location = geolocator.geocode(address)
    if location:
        folium.Marker(
            location=[location.latitude, location.longitude],
            popup=person,
            tooltip=person,
        ).add_to(map_location)
    else:
        print(f"Warning: Unable to find location for {person} - '{address}'")

# Save the map as an HTML file
map_location.save("x_unsw_whereabouts.html")

# Open the map in the default web browser
import webbrowser
webbrowser.open("x_unsw_whereabouts.html")





