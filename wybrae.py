#from tkinter.filedialog import askopenfilename
#filename_original = askopenfilename()

filename_original='RA170218.TXT'

with open(filename_original) as oldfile, open('1.txt', 'w') as newfile:
  for line in oldfile:
    if( 'X=' in line):
      newfile.write(line)
  oldfile.close()
  newfile.close()
      
with open('1.txt') as oldfile, open('2.txt', 'w') as newfile:
  for line in oldfile:
    if( not ('xxx.xxx' in line)):
      newfile.write(line)
  oldfile.close()
  newfile.close()
    
with open('2.txt') as oldfile, open('3.txt', 'w') as newfile:
  for line in oldfile:
    head, sep, tail = line.partition('Y= ')
    newfile.write(tail)
  oldfile.close()
  newfile.close()
  
with open('3.txt') as oldfile, open('4.txt', 'w') as newfile:  
  for line in oldfile:
    head, sep, tail = line.partition('    X= ')
    newfile.write(head + ' ' + tail)
oldfile.close()
newfile.close()


lat_min = 52.177804
lat_max = 52.286900
lng_min = 20.943003
lng_max = 21.107349

#min max
with open('4.txt') as oldfile, open('5.txt', 'w') as newfile:  
  for line in oldfile:
    if float(line.split()[0]) >= lat_min and float(line.split()[0]) <= lat_max and float(line.split()[1]) >= lng_min and float(line.split()[1]) <= lng_max:
      newfile.write(line)
oldfile.close()
newfile.close()



lines_seen = set() # holds lines already seen
outfile = open('wybrane.xml', "w")
outfile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
outfile.write('<markers>\n')

i=1
for line in open('5.txt', "r"):
    if line not in lines_seen:
        lines_seen.add(line)
        lat, sep, lng = line.partition('  ')
        outfile.write('    <marker id="'+repr(i))
        outfile.write('" name="')
        outfile.write(' ')#nazwa przystanku
        outfile.write('" lat="')
        outfile.write(lat)
        outfile.write(' " lng="')
        lng, sep, tail = lng.partition('\n')

        outfile.write(lng[:-2])
        outfile.write('" />\n')
        i=i+1
        
outfile.write('</markers>')
outfile.close()




























