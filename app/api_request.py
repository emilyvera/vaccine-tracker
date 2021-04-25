# import requests
import pandas as pd
import googlemaps
import os
import sqlalchemy
from yaml import load, Loader
from flask import Flask, render_template
import sys

gmaps = googlemaps.Client(key='AIzaSyBIfeeAdo_WhXbdH4_i1UdpzuLQHvLUtcM')

#CSV columns list
city_names_list = []
safety_ratings_list = []
administration_ratings_list = []
death_to_cases_ratio_list = []
latitude_list = []
longitude_list = []


conn = db.connect()
query_results = conn.execute("CALL Result2();").fetchall()
conn.close()

for i, result in enumerate(query_results):
    if i == 579 or i == 84 or i == 312 or i == 311 or i == 310:
        continue

    city_names_list.append(result[1])
    safety_ratings_list.append(result[2])
    administration_ratings_list.append(result[3])
    death_to_cases_ratio_list.append(result[4])

print('Length of cities list is ' + str(len(city_names_list)), file=sys.stdout)
print('Length of safety ratings list is ' + str(len(safety_ratings_list)), file=sys.stdout)
print('Length of administration ratings list is ' + str(len(administration_ratings_list)), file=sys.stdout)
print('Length of death to cases list is ' + str(len(death_to_cases_ratio_list)), file=sys.stdout)


for i, city_name in enumerate(city_names_list):

    # print('decoding city #' + str(i), file=sys.stdout)
    geocode_result = gmaps.geocode(city_name)

    latitude_list.append(geocode_result[0]['geometry']['location']['lat'])
    longitude_list.append(geocode_result[0]['geometry']['location']['lng'])


print('Length of latitude list is ' + str(len(latitude_list)), file=sys.stdout)
print('Length of longitude list is ' + str(len(longitude_list)), file=sys.stdout)

#Creating dataframe
dict = {'CityName': city_names_list, 'SafetyRating': safety_ratings_list, 'AdministrationRating': administration_ratings_list, 'DeathsToCasesRation': death_to_cases_ratio_list, 'Latitude': latitude_list, 'Longitude' : longitude_list}

df = pd.DataFrame(dict)
df.to_csv('geocoded_cities.csv')