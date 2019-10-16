import folium
import pandas
from pandas import ExcelWriter
from pandas import ExcelFile
import math

data = pandas.read_csv("Volcanoes.txt")
v = pandas.read_excel('all.xlsx')
lat = list(data['LAT'])
lon = list(data['LON'])
n = list(data['NAME'])
elev = list(data['ELEV'])

html = """<h4>%s</h4> Height: %d m"""

map = folium.Map(location=[-2.072371, -79.841596], zoom_start=4, tiles="OpenStreetMap")

def elev_c(e):
    if e < 1000:
        return 'green'
    elif 1000 <= e < 3000:
        return 'red'
    else:
        return 'blue'
html1 = """<h4>%</h4>"""

fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, n, elev in zip(lat, lon, n, elev):
    iframe = folium.IFrame(html=html % (n, elev), width=200, height=100)
    fgv.add_child(folium.Circle(location=[lt, ln], popup=folium.Popup(iframe), color=elev_c(elev), radius=1000))

for i in v.index:
    #name = v['Dominant Rock Type'][i]
    iframe = folium.IFrame(html=html % (v['Volcano Name'][i], v['Elevation (m)'][i]), width=200, height=100)
    if (math.isnan(v['Latitude'][i])):
        pass
    else:
        fgv.add_child(folium.Circle(location=[v["Latitude"][i], v['Longitude'][i]], popup=folium.Popup(iframe), color='blue', radius=2000))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'yellow'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
