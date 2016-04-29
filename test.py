from threading import Thread
import requests
import time
import twitter

#def tweet():

def test(siteurl, sitename):
    currentstatus = 1
    while True:
        try:
            r = requests.get(siteurl, timeout=20)
            if r.status_code == 200:
                if currentstatus == 1:
                    print sitename, "is still up"
                    time.sleep(60)
                else:
                    print sitename, "is back up"
                    time.sleep(60)
                    currentstatus = 1
            else:
                if currentstatus == 0:
                    print sitename, "is still down"
                    time.sleep(60)
                else:
                    print sitename, "is down"
                    time.sleep(60)
                    currentstatus = 0

        except requests.Timeout:
            if currentstatus == 1:
                time.sleep(60)
            elif currentstatus == 0:
                print sitename, "is down"
                time.sleep(60)
                currentstatus = 1

def tracker():
    test('http://tracker.bfscapital.com', 'tracker')

def docloc():
    test('https://documents.bfscapital.com', 'doclocator')

thread1 = Thread(target = tracker)
thread2 = Thread(target = docloc)

if __name__ == '__main__':
    thread1.start()
    thread2.start()
