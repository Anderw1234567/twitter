import twitter



api = twitter.Api(consumer_key="zdbHzOX0DjaGY3scfr8FMXYdr",
                  consumer_secret="uMqkCX2LGGDopWhrnZqg0zm25fzxDrvLbI4lutbxmLa7Ua7ifd",
                  access_token_key="834009169-0pAvvfprthhrVPUsgEark1LG7kYOCa29iS6Hco1d",
                    access_token_secret="pFeKRcJg84rvMepl4dZv23B061gXK7N2wOfB5dHBPVWts")

myFollowersList = []
myFollowers = api.GetFollowers('andruhh6')
for myFollower in myFollowers:
    name = myFollower.screen_name
    myFollowersList.append(name)
    print("BASE FOLLOWER: " + name)
    followerFollowerList = []
    for folFollower in myFollowersList:
        folFol = api.GetFollowers(folFollower)
        for fFol in folFol:
            followerFollowerList.append(fFol.screen_name)
            print("{} is followed by: {}".format(name, fFol.screen_name))
