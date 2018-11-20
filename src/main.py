import discord, asyncio, configparser

config = configparser.ConfigParser()
config.read("../config/config")
token = config.get("token","discord")
env = config.get("env", "env")

client = discord.Client()
channel_list = {
    "general": "508825694567137299",
    "bot_test" : "512270615202365441"
}

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    print(message)
    if message.content.startswith('/hey'):
        await client.send_message(message.channel, "(っ'-')╮ =͟͟͞͞ ")
    elif message.content.startswith('/github'):
        await client.send_message(message.channel, "https://github.com/42krums/manju_bot")
    # --- test code ---
    elif message.content.startswith('/test') and env == 'dev':
        await on_member_join(message)

@client.event
async def on_member_join(member):
    send_channel = client.get_channel(channel_list["general"])
    print(send_channel, 'a')
    await client.send_message(send_channel, "工科大まんじゅうおいしい！一番好きなまんじゅうです！ \n (っ'-')╮ =͟͟͞͞ ")

client.run(token)