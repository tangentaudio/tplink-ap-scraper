import sys
import requests
import json
import hashlib
from prettytable import PrettyTable


def scrape(address, username, password):

    url_base = 'http://' + address
    pw_hash = hashlib.md5(password.encode('utf-8')).hexdigest().upper()
    print(pw_hash)

    with requests.Session() as session:

        try:
            r = session.post(url_base + '/login.json', data={'operation':'read'})
            r = session.post(url_base + '/', data={'username':username, 'password':pw_hash})
            r = session.get(url_base + '/data/monitor.client.client.json?operation=load&_=1')
            
            o = json.loads(r.content)
            
            if 'notLogin' in o and o['notLogin'] is True:
                print('login failure')
                return False
            elif 'data' in o:
                return o['data']
            else:
                print('other response failure')
                return False

        except:
            print('request failure: ', sys.exc_info())
            return False
            

ap = scrape('192.168.0.2', 'user', 'password')

if ap:
    t = PrettyTable(['AP', 'SSID', 'MAC', 'IP', 'Device Name', 'Active Time'])

    for client in ap:
        t.add_row([client['AccessPoint'], client['SSID'], client['MAC'], client['IP'], client['DeviceName'], client['ActiveTime']])

    print(t)


