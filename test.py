from threading import Thread
import requests
import time
import twitter

def tweet(sitename, updown):
    TOKEN=""
    TOKEN_KEY=""
    CON_SEC=""
    CON_SEC_KEY=""

    my_auth = twitter.OAuth(TOKEN,TOKEN_KEY,CON_SEC,CON_SEC_KEY)
    twit = twitter.Twitter(auth=my_auth)

    tweet = sitename, "is", updown

    twit.statuses.update(status=tweet)

def test(siteurl, sitename):
    updown = ""
    currentstatus = 1
    while True:
        try:
            r = requests.get(siteurl, timeout=20)
            if r.status_code == 200:
                if currentstatus == 1:
                    #print sitename, "is still up"
                    time.sleep(60)
                else:
                    #print sitename, "is back up"
                    updown = 'up'
                    tweet(sitename)
                    currentstatus = 1
                    time.sleep(60)
            else:
                if currentstatus == 0:
                    #print sitename, "is still down"
                    time.sleep(60)
                else:
                    #print sitename, "is down"
                    updown = 'down'
                    tweet(sitename, updown)
                    currentstatus = 0
                    time.sleep(60)

        except requests.Timeout:
            if currentstatus == 1:
                time.sleep(40)
            elif currentstatus == 0:
                #print sitename, "is down"
                updown = 'down'
                tweet(sitename, updown)
                time.sleep(40)
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
