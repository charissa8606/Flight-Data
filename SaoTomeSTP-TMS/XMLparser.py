import xml.etree.ElementTree as ET

##create file to store extracted data
file = open("extractedData.txt", "w+")

##parse xml tree
myTree = ET.parse("TMS2019DeparturesClean.txt")

##get root node
myRoot = myTree.getroot()

##iterates through all tags named flightStatus
for x in myRoot.iter('flightStatus'):
    arrival = x.find('arrivalAirportFsCode').text ##gets arrival airport code
    departure = x.find('departureDate') 
    date = departure.find('dateLocal').text ##gets departure time
    export = arrival + " " + date + "\n" ##generate string for export
    file.write(export) ##write to new file

file.close()
