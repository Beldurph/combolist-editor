import requests
import json
import uuid
import os

premiumplus = ['11', '12', '93', '96', '97', '99', '100', '101', '4', '3', '6', '94', '92']

def ctoauth():
    if os.path.isfile('key.dat'):
        current_hwid = uuid.getnode()
        f = open('key.dat', 'r')
        auth = f.read()
        data = {
            "a": "auth",
            "k": str(auth),
            "hwid": str(current_hwid)
        }
        checkauth = requests.post('https://cracked.to/auth.php', data=data)
        with checkauth:
            json1 = json.loads(checkauth.text)
            if '"auth":true' in checkauth.text:
                #Upgraded users check starts here
                pass
                #Upgraded users check ends here
            else:
                print(checkauth.text)
                exit()
    else:
        authkey = str(input('Insert Cracked.to Auth Key: '))
        current_hwid = uuid.getnode()

        data = {
            "a": "auth",
            "k": str(authkey),
            "hwid": str(current_hwid)
        }

        checkauth = requests.post('https://cracked.to/auth.php', data=data)

        with checkauth:
            json2 = json.loads(checkauth.text)
            if '"auth":true' in checkauth.text:
                #Upgraded users check starts here
                pass
                #Upgraded users check ends here
            else:
                print(checkauth.text)
                exit()