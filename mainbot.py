import discord
import json
import random as rand
import stalkerlog as stalker
#stalkerlog = json.loads('stalkerstuff.json')
TOKEN = 'NTI0MTM3MjgzMDIxMDQ1NzYw.DvsyOg.kasDn0HmUT4fAYkeIHo7pibPkG4'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    print(message.author,message.content)
    name = str(message.author)
    content = str(message.content)
    #data = {name:content}
    #print(data)
    stalker.logit(name,content)
    if message.author == client.user:
        return

    #standard greet bullshit
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    #Completely accurate squaring robot
    if message.content.startswith('!square'):
        sqrt = "That's not a number."
        try:
            num = int(message.content[7:])
            sqrt = (num*num)+rand.randint(-50000,50000)
        except:
            print("!square tried without a number.")

        msg = sqrt,'{0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!remember'):
        mem = json.load(open('stalkerstuff.json'))
        mem1 = rand.choice(list(mem.items()))
        mem2 = []
        for thing in mem1:
            if len(mem2) > 2000:
                print('discarding leftover datas')
            else:
                mem2.append(thing)
        await client.send_message(message.channel, mem2)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
