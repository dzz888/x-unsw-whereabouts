import gspread
import folium
from geopy.geocoders import Nominatim

# Function to get geolocation from an address
def get_location(address):
    geolocator = Nominatim(user_agent="map_location_app")
    location = geolocator.geocode(address)
    return location.latitude, location.longitude if location else None

# Function to read the Google Sheets document URL from an external file
def read_google_sheets_url(file_path):
    with open(file_path, "r") as file:
        url = file.read().strip()
    return url

# Function to read data from a publicly accessible Google Sheets document
def read_google_sheets(sheet_url, sheet_name):
    gc = gspread.service_account()
    sheet = gc.open_by_url(sheet_url).worksheet(sheet_name)
    data = sheet.get_all_records()
    return data

GOOGLE_SHEET_URL_FILE = "google_sheets_url.txt"
GOOGLE_SHEET_URL = read_google_sheets_url(GOOGLE_SHEET_URL_FILE)
SHEET_NAME = "Sheet1"

# Read data from the publicly accessible Google Sheets document
people_data = read_google_sheets(GOOGLE_SHEET_URL, SHEET_NAME)

# Create a folium map centered on the first person's location
first_person_address = people_data[0]['Address']
first_person_location = get_location(first_person_address)

if first_person_location:
    map_location = folium.Map(location=first_person_location, zoom_start=10)

    # Create a dictionary to store locations and corresponding people
    location_dict = {}

    # Add markers for each person's location
    for person_data in people_data:
        person = person_data['Name']
        address = person_data['Address']
        location = get_location(address)
        if location:
            # Check if the location already exists in the dictionary
            if location in location_dict:
                location_dict[location].append(person)
            else:
                location_dict[location] = [person]

    # Add markers for each unique location
    for location, people in location_dict.items():
        popup_text = ", ".join(people)
        folium.Marker(
            location=location,
            popup=popup_text,
            tooltip=popup_text,
        ).add_to(map_location)

    # Save the map as an HTML file
    map_location.save("x_unsw_whereabouts.html")

    # Open the map in the default web browser
    import webbrowser
    webbrowser.open("x_unsw_whereabouts.html")
    
else:
    print(f"Error: Unable to find location for the first person - '{first_person_address}'")
    




