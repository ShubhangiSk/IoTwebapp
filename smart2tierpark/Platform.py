import urllib3
import json
import time
from django.utils import timezone
class Platform:
    def __init__(self):
            http = urllib3.PoolManager()
            url="http://api.thingspeak.com/channels/365105/feeds/last.json?api_key=TLHYRRGOCG7N1NH0"
            url1="http://api.thingspeak.com/channels/364324/feeds/last.json?api_key=4FYMMZT7GQR48HIQ"
            r = http.request('GET', url)
            r1 = http.request('GET', url1)
            response = r.data
            response1 = r1.data
            data=json.loads(response)
            data1=json.loads(response1)
            self.aj = data['created_at']
            self.sv = data['field1']
            self.aj1 = data['created_at']
            self.sv1 = data['field1']
            
            self.start_park=timezone.now()
            time.sleep(5)
            self.getplatformnumber()
    def getplatformnumber(self):
        if int(self.sv1)>30:
            self.pnum="Platform 1"
            self.pn="Go to platform 1."
        elif int(self.sv)>30:
            self.pnum="Platform 2"
            self.pn="Go to platform 2."
        else:
            self.pnum="none"
            self.pn="Parking full."
