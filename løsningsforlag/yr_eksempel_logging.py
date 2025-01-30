#!/usr/bin/env python3
import logging
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-log-level', type=str,default='INFO',required=False, help='Log level, DEBUG, INFO, WARNING, ERROR')
args = parser.parse_args()

logging.basicConfig(level=args.log_level, filename='../filer/logger.txt', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


logger.info("Åpner filer for write")
t = open('../filer/temperatur.txt', 'w', encoding="utf-8")
v = open('../filer/vind.txt', 'w', encoding="utf-8")

try:
    logger.info("Skriver overskrift")
    t.write("Jørstadmoen temperatur\n")
    v.write("Jørstadmoen vind\n")
except IOError as e:
    print("Feil i å skrive til fil %s" ,e)
    logger.error("Feil i å skrive til fil  %s" ,e)

logger.info("Henter vær fra YR API")
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
        logger.debug("Skriver lufttemperatur til fil")
        t.write(f"Tid: {time['time']}\n")
        t.write(f"Lufttemperatur: {time['data']['instant']['details']['air_temperature']} °C\n")

        logger.debug("Skriver vindhastighet til fil")
        v.write(f"Tid: {time['time']}\n")
        v.write(f"Vindhastighet: {time['data']['instant']['details']['wind_speed']} m/s\n")

    except IOError as e:
        print("Feil i å appende til fil")
        logger.error("Feil i å appende fil %s" ,e)

try:    
    logger.info("Lukker filer")
    t.close()
    v.close()
except IOError as e:
    print("Feil i å lukke fil")
    logger.error("Feil i å lukke fil %s" ,e)