import tweepy, json
from flask import Flask

auth = tweepy.AppAuthHandler("zdbHzOX0DjaGY3scfr8FMXYdr", "uMqkCX2LGGDopWhrnZqg0zm25fzxDrvLbI4lutbxmLa7Ua7ifd")
api = tweepy.API(auth)

flaskApp = Flask(__name__)

#redirect_url = auth.get_authorization_url()
#auth.get_access_token("834009169-0pAvvfprthhrVPUsgEark1LG7kYOCa29iS6Hco1d")
#api = twitter.Api(consumer_key="zdbHzOX0DjaGY3scfr8FMXYdr",
#                  consumer_secret="uMqkCX2LGGDopWhrnZqg0zm25fzxDrvLbI4lutbxmLa7Ua7ifd",
#                  access_token_key="834009169-0pAvvfprthhrVPUsgEark1LG7kYOCa29iS6Hco1d",
#                  access_token_secret="pFeKRcJg84rvMepl4dZv23B061gXK7N2wOfB5dHBPVWts")

#def isValid(str):
#    return (str.lower() in 'abcdefghijklmnopqrstuvwxyz') and (str in ',./;[]=-<>?:"{}|!+@_#)$(%*^&0123456789')


@flaskApp.route('/')
def hello_world():
    return 'Hello, World!'

@flaskApp.route('/nicksfollowers')
def nicks_followers():
    fols = api.followers_ids("NickT231")
    for u in fols:
        user = api.get_user(u)
        print(user.screen_name)
    return 'nicks followers!'
    

def isValid(str):
    for c in str:
        if c == '/':
            return False
    return True


brett = 923685787
me = 834009169
nick = 809484452
listOfUsers = [834009169,#My Own Account
               809484452 #Nicks account
              ]

fols = api.followers_ids("NickT231")
print("we just got nicks followers btw")


if __name__ == '__main__':
    flaskApp.run()
#for page in paginate(fols, 100):
#for u in fols:
    #user = api.get_user(u)
   # print(user.screen_name)
#print(fols)

#print(api.rate_limit_status())
#followers = tweepy.Cursor(api.followers("NickT231")).items()
#for i in range(0,2):
#    print(followers.next())
##
##users = api.followers("NickT231")
##nicksFollowers = []
##for u in users:
##    print(u.name)
##
##    try:
##        nicksFollowers.append(api.followers(u.name))
##    except:
##        print("fuck u sunny")
##
##    print(len(nicksFollowers))        
 #   for f in nicksFollowers:
 #       print(" Nicks Follower " + u.name + " is followed by " + f.name)
        
    
#    temp = s
#    if isValid(s.text):        
#        print(s.text)
#    print()
