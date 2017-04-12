import csv
import simplekml #http://www.simplekml.com/en/latest/
import sys
import urllib2
import json


reload(sys)
sys.setdefaultencoding('utf-8')

csv_number_column = 0
csv_date_column = 1
csv_address_column = 2
csv_cost_column = 3
csv_sqm_column = 4
csv_cost_per_sqm_column = 5

url_prefix="https://maps.googleapis.com/maps/api/geocode/json?address="
url_address="Targowa+33B"
url_postfix="&key=AIzaSyDh4DBgfTfNtRSyohUdyGAY76SV9BnIkU8"
response=urllib2.urlopen(url_prefix+url_address+url_postfix).read()
data = json.loads(response)
lat=data['results'][0]['geometry']['location']['lat']
lng=data['results'][0]['geometry']['location']['lng']
print(lat)
print(lng)

inputfile = csv.reader(open('data.csv','r'))
kml=simplekml.Kml()

for row in inputfile:
  if(row[csv_address_column]!=''): #remove empty lines
    pnt = kml.newpoint(name=row[csv_address_column])
    pnt.address = row[csv_address_column]
    pnt.description = " address: " + row[csv_address_column] + " area: " + row[csv_sqm_column] + "sqm"
    url_address=row[csv_address_column]
    url_address=url_address.replace(" ", "+")
    print(row[csv_address_column])
    print(url_prefix+url_address+url_postfix)
    response=urllib2.urlopen(url_prefix+url_address+url_postfix).read()
    data = json.loads(response)
    lat=data['results'][0]['geometry']['location']['lat']
    lng=data['results'][0]['geometry']['location']['lng']
    pnt.coords=[(lat,lng)]
    pnt.address=row[csv_address_column]

kml.save('data.kml')