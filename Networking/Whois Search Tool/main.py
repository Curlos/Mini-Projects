from ipwhois import IPWhois
from pprint import pprint

# Sample IP Address: 74.125.225.229
ip_address = input('Enter an IP address: ')
obj = IPWhois(ip_address)
results = obj.lookup_rdap(depth=1)
pprint(results)
