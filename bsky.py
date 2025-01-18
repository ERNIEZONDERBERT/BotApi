from atproto import Client
import os

client = Client()
client.login('erniezonderbert.bsky.social', os.environ['BSKY_PASSWORD'])

follows = client.get_follows(actor='testerboi.bsky.social', limit=100)
print(len(follows.follows))

with open('bots.txt', 'w') as file:
    for follow in follows.follows[:50]:
        file.write(follow.handle + '\n')