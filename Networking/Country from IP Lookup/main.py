import ipinfo
import os
from dotenv import load_dotenv
from pprint import pprint
import json

load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")


def countryFromIPLookup():
    ''' Enter an IP address and find the country that IP is registered in. '''

    handler = ipinfo.getHandler(ACCESS_TOKEN)
    # Sample IP Address: 216.239.36.21
    ip_address = input('Enter an IP Address: ')
    details = handler.getDetails(ip_address)
    return details.country


pprint(countryFromIPLookup())
