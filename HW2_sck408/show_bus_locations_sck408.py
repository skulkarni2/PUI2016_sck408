
import csv
import json
import sys
import urllib2

#def main():
# read the json data from url provided using the following key
#key : 54f7c4f7-4b0e-48d2-a8a4-867374a1ae4a
# use upper() to make it into uppercase. 

if __name__=='__main__':
	url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" %(sys.argv[1], sys.argv[2].upper())
	urlData = urllib2.urlopen(url)
	data = json.load(urlData)

	BusAc = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
	
BusLine = BusAc[0]["MonitoredVehicleJourney"]["PublishedLineName"]
print "Bus Line : %s" %(BusLine)

#print number of buses 
num_of_bus = len(data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"])
print "Number of Active Buses: %s" %(num_of_bus)

# get the Lat, Lon for each bus 

index = 0 
for Bus in BusAc:
	BusNumber = index
	Latitude = Bus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
	Longitude = Bus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
	index += 1
	print "Bus %s is at Latitude %s and Longitude %s" %(BusNumber, Latitude, Longitude)


