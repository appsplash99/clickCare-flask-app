# Importing required libraries
from googleplaces import GooglePlaces
# from pprint import pprint

# This is the way to make api requests
# using python requests library

import geocoder

g = geocoder.ip('me')
print(g.latlng)
my_lat_lng = {'lat': g.latlng[0], 'lng': g.latlng[1]}

# Use your own API key for making api request calls
API_KEY = 'AIzaSyBr8V0XkaNFYkNXcP6eJc76b6YutvizwNw'

# Initialising the GooglePlaces constructor
google_places = GooglePlaces(API_KEY)


def generate_covid_centers_DATA():
    #### txt_search api
    query_result = google_places.text_search(
        # lat_lng ={'lat': 46.1667, 'lng': -1.15},
        query='covid testing',
        lat_lng=my_lat_lng,
        radius=5000,
    )

    # If any attributions related
    # with search results print them
    if query_result.has_attributions:
        print(query_result.html_attributions)

    # storing returned data
    # covid_centers_list
    covid_centers_list = []

    # covid_centers_list = [
    #      { name: xyz,
    #        local_phone: 5645464,
    #        international_phone: +85431
    #      },
    #      { name: pqr,
    #        local_phone: 123456,
    #        international_phone: +99999
    #      }
    # ]

    # print(query_result.places)

    # Iterate over the search results
    # Iterate over the search results
    counter = 0
    for place in query_result.places:
        each_place_dict = {}
        if (counter == 5): break
        counter += 1
        place.get_details()

        # creating a place object of single place
        each_place_dict['1name'] = place.name,
        each_place_dict['2local_phone_num'] = place.local_phone_number,
        each_place_dict['3international_phone_num'] = place.international_phone_number,

        # appending single place dict
        covid_centers_list.append(each_place_dict)

    # printing list data in terminal
    # pprint(covid_centers_list)
    # returning final data
    return covid_centers_list