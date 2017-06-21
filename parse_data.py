import csv
import simplekml #http://www.simplekml.com/en/latest/
import sys
import urllib2
import json
 
def check():
    found = False
    for line in already_added_file:
        if address_full in line:
            found = True
            break

    return found

def point_not_present():
    already_added_file.write(address_full + '\n')
    print(url_prefix+address_for_search+url_postfix)
    response=urllib2.urlopen(url_prefix+address_for_search+url_postfix).read()
    data = json.loads(response)
    lat=data['results'][0]['geometry']['location']['lat']
    lng=data['results'][0]['geometry']['location']['lng']
    pnt.coords=[(lng,lat)]
    pnt.address=row[csv_address_column]

##################################################
reload(sys)
sys.setdefaultencoding('utf-8')

ALWAYS_OVERRIDE = False#True
csv_number_column       = 0
csv_date_column         = 1
csv_address_column      = 2
csv_cost_column         = 3
csv_sqm_column          = 4
csv_cost_per_sqm_column = 5
kw_number_column        = 6

already_in_database_counter = 0
new_in_database_counter     = 0

url_prefix="https://maps.googleapis.com/maps/api/geocode/json?address="
url_postfix="&key=AIzaSyDh4DBgfTfNtRSyohUdyGAY76SV9BnIkU8"

inputfile = csv.reader(open('data.csv','r'))
already_added_file = open('already_added.txt','r+w+a')
kml=simplekml.Kml()


for row in inputfile:
  if(row[csv_address_column]!=''): #remove empty lines
    pnt = kml.newpoint(name=row[csv_address_column])
    pnt.address = row[csv_address_column]
    pnt.description = row[csv_cost_per_sqm_column] + "zl/m2<br/>" + row[csv_sqm_column] + "m2<br/>data - " + row[csv_date_column] + " " + row[kw_number_column]
        
    price = int(row[csv_cost_per_sqm_column])

    if price < 5000:
        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/paddle/blu-blank.png'
    elif price < 6000:
        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/paddle/grn-blank.png'
    elif price < 7000:
        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/paddle/ylw-blank.png'
    elif price < 8000:
        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/paddle/orange-blank.png'
    elif price < 9000:
        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/paddle/pink-blank.png'
    else:
        pnt.style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/paddle/red-blank.png'

    address_full="Warszawa, "+row[csv_address_column]
    address_full=address_full.replace(" ", "+")

    numer_mieszkania = address_full.split('/')[-1]
    if len(numer_mieszkania) != len(address_full):
        address_for_search = address_full[:-(len(numer_mieszkania)+1)]
    else: 
        address_for_search = numer_mieszkania[:-2] #usinamy 2 ostatnie znaki z dupy

    if ~check() or ALWAYS_OVERRIDE:
        new_in_database_counter = new_in_database_counter+1
        point_not_present()
    else:
        already_in_database_counter = already_in_database_counter+1


kml.save('data.kml')

print "Already in database " + str(already_in_database_counter)
print "NEW " + str(new_in_database_counter) 
already_added_file.close()
