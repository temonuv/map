import csv
import simplekml #http://www.simplekml.com/en/latest/
import sys
import urllib2
import json
 
def check():
        found = False
        for line in already_added_file:
            if url_address in line:
                found = True
                break

        return found

def point_not_present():
        already_added_file.write(url_address + '\n')
        #print(row[csv_address_column])
        response=urllib2.urlopen(url_prefix+url_address+url_postfix).read()
        data = json.loads(response)
        lat=data['results'][0]['geometry']['location']['lat']
        lng=data['results'][0]['geometry']['location']['lng']
        #print(lat)
        #print(lng)
        pnt.coords=[(lng,lat)]
        pnt.address=row[csv_address_column]

reload(sys)
sys.setdefaultencoding('utf-8')

NADPISUJ_PLIKI=1

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

inputfile = csv.reader(open('data.csv','r'))
already_added_file = open('already_added.txt','r+w+a')
kml=simplekml.Kml()

already_in_database_counter=0;
new_in_database_counter=0;


for row in inputfile:
  if(row[csv_address_column]!=''): #remove empty lines
    pnt = kml.newpoint(name=row[csv_address_column])
    pnt.address = row[csv_address_column]
    pnt.description = "cena/m2 " + row[csv_cost_per_sqm_column] + " area: " + row[csv_sqm_column]
    url_address="Warszawa, "+row[csv_address_column]
    url_address=url_address.replace(" ", "+")

    found = check()
    if check():
        already_in_database_counter = already_in_database_counter+1
    else:
        print(url_address)
        new_in_database_counter = new_in_database_counter+1
        point_not_present()

kml.save('data.kml')

print "Already in database " + str(already_in_database_counter)
print "NEW " + str(new_in_database_counter) 
already_added_file.close()
