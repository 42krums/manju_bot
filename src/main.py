import discord, asyncio, configparser

config = configparser.ConfigParser()
config.read("../config/token")
token = config.get("token","discord")

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(message)

@client.event
async def on_message(message):
    if message.content.startswith('こんにちは'):
        await client.send_message(message.channel, "(っ'-')╮ =͟͟͞͞ ")
        // 工科大まんじゅう.jpgを添付

client.run(token)