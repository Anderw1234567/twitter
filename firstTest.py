import tweepy

auth = tweepy.AppAuthHandler("zdbHzOX0DjaGY3scfr8FMXYdr", "uMqkCX2LGGDopWhrnZqg0zm25fzxDrvLbI4lutbxmLa7Ua7ifd")
#redirect_url = auth.get_authorization_url()
#auth.get_access_token("834009169-0pAvvfprthhrVPUsgEark1LG7kYOCa29iS6Hco1d")
api = tweepy.API(auth)
#api = twitter.Api(consumer_key="zdbHzOX0DjaGY3scfr8FMXYdr",
#                  consumer_secret="uMqkCX2LGGDopWhrnZqg0zm25fzxDrvLbI4lutbxmLa7Ua7ifd",
#                  access_token_key="834009169-0pAvvfprthhrVPUsgEark1LG7kYOCa29iS6Hco1d",
#                  access_token_secret="pFeKRcJg84rvMepl4dZv23B061gXK7N2wOfB5dHBPVWts")

#def isValid(str):
#    return (str.lower() in 'abcdefghijklmnopqrstuvwxyz') and (str in ',./;[]=-<>?:"{}|!+@_#)$(%*^&0123456789')



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


tweets = api.followers(nick)
for s in tweets:
    print(s)
#    temp = s
#    if isValid(s.text):        
#        print(s.text)
#    print()
