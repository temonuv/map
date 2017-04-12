import csv
import simplekml #http://www.simplekml.com/en/latest/
import sys
import urllib2

reload(sys)
sys.setdefaultencoding('utf-8')

csv_number_column = 0
csv_date_column = 1
csv_address_column = 2
csv_cost_column = 3
csv_sqm_column = 4
csv_cost_per_sqm_column = 5
url="https://maps.googleapis.com/maps/api/geocode/json?address=Targowa+33B&key=AIzaSyDh4DBgfTfNtRSyohUdyGAY76SV9BnIkU8"

content=urllib2.urlopen(url).read()
print(content)

inputfile = csv.reader(open('data.csv','r'))
kml=simplekml.Kml()

for row in inputfile:
  if(row[csv_address_column]!=''): #remove empty lines
    pnt = kml.newpoint(name=row[csv_address_column])
    pnt.address = row[csv_address_column]
    pnt.description = " address: " + row[csv_address_column] + " area: " + row[csv_sqm_column] + "sqm"
    pnt.coords=[(row[3],row[4])]
    pnt.address=row[csv_address_column]

kml.save('data.kml')