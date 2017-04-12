lines_seen = set() # holds lines already seen
outfile = open('moje.xml', "w")
outfile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
outfile.write('<markers>\n')

i=1
for line in open('moje.txt', "r"):
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




























