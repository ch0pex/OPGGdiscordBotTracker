import discord
import cassiopeia as cass
from screenshot import screenshot_op_gg
import aux
from jsonstorage import Storage
from discord.ext import tasks
import asyncio
import time

discord.Intents.default()
client = discord.Client()
cass.set_riot_api_key(RIOT_KEY)
storage = Storage()
channel_default = None
print(storage)

@client.event
async def on_ready():
    print(f'We gave logged in as {client.user}')
    global channel_default
    channel_default = client.get_channel(960890962052259932)




@tasks.loop(seconds = 20)
async def loop_current_game_trigger():
    global channel_default
    if channel_default:
        for i in storage.accounts:
            summoner = cass.get_summoner(name=i, region="EUW")
            print(storage)
            try:
                if summoner.current_match is not False:
                    print(storage)
                    await storage.set_bool(i, summoner.current_match.id)
                    bool_game = await storage.check_bool(i)
                    print(bool_game)
                    if not bool_game:
                        await screenshot_op_gg(summoner.name)
                        av2 = discord.Embed(title=f"Partida en curso de {summoner.name}", color=7419530)
                        file = discord.File(f"/home/acbsu/screenshots/last.png", filename="last.png")
                        av2.set_image(url=f"attachment://last.png")
                        await channel_default.send(file=file, embed=av2)
                    else:
                        print("dos games iguales")
            except:
                print(i+" no ha iniciado partida")



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('current'):
        region = await aux.message_checker(message)
        summoner = cass.get_summoner(name=message.content.split("-")[0][8:], region=region)
        if await aux.summoner_checker(message,summoner) is False:
            return
        await screenshot_op_gg(summoner.name)
        return await aux.message_embed(message,"Partida en curso: ",file_name="last.png")

    if message.content.startswith('track'):
        region = await aux.message_checker(message)
        print(region)
        summoner = cass.get_summoner(name=message.content.split("-")[0][6:], region=region)
        if summoner.exists is not False:
            print(storage.accounts)
            try:
                await storage.add_summoner(summoner.name,region)
                await aux.message_embed(message, "Otro mono mas a la lista")
            except:
                await aux.message_embed(message,"Ese usuario ya esta siendo trackeado nini")
            print(storage.accounts)
        else:
            await aux.message_embed(message,"El usuario que quieres añadir no existe pringao")


    if message.content.startswith('untrack'):
        region = await aux.message_checker(message)
        summoner = cass.get_summoner(name=message.content.split("-")[0][8:], region= region)
        if summoner.exists is not False:
            print(storage.accounts)
            try:
                await storage.delete_summoner(summoner.name)
                await aux.message_embed(message, "Ya no seguiremos mas a ese manco")
            except:
                await aux.message_embed(message, "Ese usuaro no esta siendo trackeado monkey")
            print(storage.accounts)
        else:
            await aux.message_embed(message, "Ese usuaro no existe bot")



loop_current_game_trigger.start()
client.run(DISCORD_KEY)


