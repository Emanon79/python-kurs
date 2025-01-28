import requests

headers = {'Accept': 'application/json'}
headers = {'User-Agent': 'Python Yr Example https://github.com/Emanon79/python-kurs'}
response = requests.get('https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=61.148588080805716&lon=10.386028685835068', headers=headers)
data = response.json()

t = open('../filer/temperatur.txt', 'w')
v = open('../filer/vind.txt', 'w') 

try:
    t.write("Jørstadmoen temperatur\n")
    v.write("Jørstadmoen vind\n")
    t.close()
    v.close()
except:
    print("Feil i å skrive til fil")


t = open('../filer/temperatur.txt', 'a')
v = open('../filer/vind.txt', 'a') 

    # Traverse the JSON data
for time in data['properties']['timeseries']:
    print(f"Tid: {time['time']}")
    print(f"Lufttemperatur: {time['data']['instant']['details']['air_temperature']} °C")
    print(f"Vindhastighet: {time['data']['instant']['details']['wind_speed']} m/s")
    print(f"Skydekke: {time['data']['instant']['details']['cloud_area_fraction']} %")
    print("-----")
    try: 
        t.write(f"Tid: {time['time']}\n")
        t.write(f"Lufttemperatur: {time['data']['instant']['details']['air_temperature']} °C\n")

        v.write(f"Tid: {time['time']}\n")
        v.write(f"Vindhastighet: {time['data']['instant']['details']['wind_speed']} m/s\n")

    except:
        print("Feil i å appende til fil")
try:    
    t.close()
    v.close()
except:
    print("Feil i å lukke fil")