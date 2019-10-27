import twitter

api = twitter.Api(consumer_key="zdbHzOX0DjaGY3scfr8FMXYdr",
                  consumer_secret="uMqkCX2LGGDopWhrnZqg0zm25fzxDrvLbI4lutbxmLa7Ua7ifd",
                  access_token_key="834009169-0pAvvfprthhrVPUsgEark1LG7kYOCa29iS6Hco1d",
                  access_token_secret="pFeKRcJg84rvMepl4dZv23B061gXK7N2wOfB5dHBPVWts")

myfols = api.GetFollowerIDs("andruhh6")

for follower in myfols:
    fol = api.GetUser(follower)
    print(f"{fol.name} follows {fol.followers_count} people.")
    myfolsfols = api.GetFollowerIDs(follower)
    for followersfollower in myfolsfols:
        folfol = api.GetUser(followersfollower)
        print(f"{fol.name} follows {folfol.name} who follows {folfol.followers_count} people.")
