import bluetooth

class bluetooth_discover():
    def find_services(self, addr):
        #find services of specified mac address
        services = bluetooth.find_service(address=addr)
        for service in services:
            print "{:-<40s}Port {}".format(service['name'], service['port'])

    def find_nearby_devices(self, list_services=False):
        #find nearby devices with names and classes(type of device)
        #check docs for specification of CoD (class of device)
        #the individual bits means different things
        print "Searching for devices..."
        try:
            self.nearby = bluetooth.discover_devices(lookup_names=True, lookup_class=True, flush_cache=True)
            print "Devices Found: {:d}".format(len(self.nearby))
            #prepare list of strings each with length 24
            bclass_str = []
            for addr, name, bclass in self.nearby:
                bclass_str.append("{:{fill}24b}".format(bclass, fill='0'))
            #print the results
            print "-"*100
            print "{:20s}{:20s}{:15s}{:12s}{:12s}{:s}".format("", "", "Service", "Maj Device", "Min Device", "Format")
            print "{:20s}{:20s}{:15s}{:12s}{:12s}{:s}".format("MAC ID", "Device Name", "Class", "Class", "Class", "Spec")
            print "-"*100
            for i in range(0, len(bclass_str)):
                print "{:20s}{:20.20s}{:15s}{:12s}{:12s}{:s}".format(self.nearby[i][0],
                    self.nearby[i][1], bclass_str[i][:11], bclass_str[i][11:16], bclass_str[i][16:22], bclass_str[i][22:])
            print "-"*100
            print "-"*100
            
            if list_services == True:
                print "\nListing all services..."
                print "~"*50
                for addr, name, bclass in self.nearby:
                    print "Services for {} ({}):".format(addr, name)
                    self.find_services(addr)
                    print "~"*50
                    
        except Exception as e:
            print "ERROR: Please ensure bluetooth is on"
            print "Details:", e

if __name__ == '__main__':
    d = bluetooth_discover()
    d.find_nearby_devices(True)
