import csv
import simplekml
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

inputfile = csv.reader(open('data.csv','r'))
kml=simplekml.Kml()

for row in inputfile:
  if(row[4]!=''): #remove empty lines
    kml.newpoint(name=row[2], coords=[(row[3],row[4])])
    kml.description = "This is a description"

kml.save('data.kml')