import requests
import time

derp = 0
''' function to monitor up time '''
while True:
    try:
        r = requests.get('http://tracker.bfscapital.com', timeout=20)
        if r.status_code == 200:
            if derp == 0:
                print "Tracker is up"
                time.sleep(60)
            elif derp == 1:
                print "Tracker is back up"
                time.sleep(60)
                derp = 0
        else:
            if derp == 1:
                time.sleep(60)
            elif derp == 0:
                print "Tracker is down"
                time.sleep(60)
                derp = 1

    except requests.Timeout:
        if derp == 1:
            time.sleep(60)
        elif derp == 0:
            print "Tracker is down"
            time.sleep(60)
            derp = 1
