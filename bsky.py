from atproto import Client
import os

client = Client()
client.login('erniezonderbert.bsky.social', os.environ['BSKY_PASSWORD'])
# client.login('testerboi.bsky.social', 'hC%@MN8cWwRi$2')

# data = client.get_profile(actor='internethippo.bsky.social')
# did = data.did
# display_name = data.display_name

follows = client.get_follows(actor='testerboi.bsky.social', limit=100)
print(len(follows.follows))

# for follow in follows.follows:
#     print(follow.handle)
#
with open('bots.txt', 'w') as file:
    for follow in follows.follows[:50]:
        file.write(follow.handle + '\n')