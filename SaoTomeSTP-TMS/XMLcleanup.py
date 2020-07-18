tempFile = open("TMS2019DeparturesClean.txt", "w+")
sourceFile = open('TMS2019Departures.txt', 'r+')
line = sourceFile.readline()

line = line.replace('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>','')

tempFile.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><root>' + line + '</root>')
sourceFile.close()
tempFile.close()

