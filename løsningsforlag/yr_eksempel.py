#!/usr/bin/env python3
import requests
from datetime import datetime

def log(melding):
    try:
        with open('../filer/log.txt', 'a') as l:
            l.write(datetime.now().strftime("%d-%m-%Y-%H:%M:%S") + ": " + melding)
            l.write('\n')
    except:
        print("Feil i å skrive til log")


log("Åpner filer for write")
t = open('../filer/temperatur.txt', 'w')
v = open('../filer/vind.txt', 'w') 

try:
    log("Skriver overskrift")
    t.write("Jørstadmoen temperatur\n")
    v.write("Jørstadmoen vind\n")
   
except:
    print("Feil i å skrive til fil")

log("Henter vær fra YR API")
headers = {'Accept': 'application/json'}
headers = {'User-Agent': 'Python Yr Example https://github.com/Emanon79/python-kurs'}
response = requests.get('https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=61.148588080805716&lon=10.386028685835068', headers=headers)
data = response.json()

    # Traverse the JSON data
for time in data['properties']['timeseries']:
    print(f"Tid: {time['time']}")
    print(f"Lufttemperatur: {time['data']['instant']['details']['air_temperature']} °C")
    print(f"Vindhastighet: {time['data']['instant']['details']['wind_speed']} m/s")
    print(f"Skydekke: {time['data']['instant']['details']['cloud_area_fraction']} %")
    print("-----")
    try: 
        log("Skriver lufttemperatur til fil")
        t.write(f"Tid: {time['time']}\n")
        t.write(f"Lufttemperatur: {time['data']['instant']['details']['air_temperature']} °C\n")

        log("Skriver vindhastighet til fil")
        v.write(f"Tid: {time['time']}\n")
        v.write(f"Vindhastighet: {time['data']['instant']['details']['wind_speed']} m/s\n")

    except:
        print("Feil i å appende til fil")
try:    
    log("Lukker filer")
    t.close()
    v.close()
except:
    print("Feil i å lukke fil")