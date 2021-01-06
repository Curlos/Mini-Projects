from ipwhois import IPWhois
from pprint import pprint

def whoisSearchIPData():
    ''' Enter an IP or host address and have it look it up through whois and return the results to you. '''

    # Sample IP Address: 74.125.225.229
    ip_address = input('Enter an IP address: ')
    obj = IPWhois(ip_address)
    results = obj.lookup_rdap(depth=1)
    return results

pprint(whoisSearchIPData())
