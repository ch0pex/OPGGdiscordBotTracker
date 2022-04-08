import discord
import cassiopeia as cass
from screenshot import screenshot_op_gg




intents = discord.Intents( guilds=True,members=True,presences=True)
client = discord.Client(intents=intents)
cass.set_riot_api_key('RGAPI-b237731c-554c-4112-a58b-303fc6193ef1')

REGIONS = ['EUW','EUNE','BR','JP', 'KR', 'LAN','LAS','NA','OCE','RU','TR']


@client.event
async def on_ready():
    print(f'We gave logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        print("Hola")
        return
    if message.content.startswith('current'):
        if "-" in message.content:
            region = message.content.split("-")[1]
            if  region not in REGIONS:
                regions_str='Region introducida no valida, prueba con:'
                for i in REGIONS:
                    regions_str += REGIONS[i] + "\n"
                return await message.channel.send(regions_str);

        else:
            region = REGIONS[0]
        summoner = cass.get_summoner(name=message.content.split("-")[0][8:], region=region)
        if summoner.exists is False:
            return await message.channel.send(f'El usuario "{summoner.name}" no existe :(')
        try:
            summoner.current_match
        except:
            return await message.channel.send(f'{summoner.name} no esta en partida ahora mismo -.-')
        screenshot_op_gg(summoner.name)
        av2 = discord.Embed(title="Partida en curso: ", color=7419530)
        file = discord.File("/home/acbsu/screenshots/last.png", filename="last.png")
        av2.set_image(url=f"attachment://last.png")
        await message.channel.send(file=file, embed=av2)

print("hola")
client.run('OTYwNTc2MjQ3NDA5Mjk5NTE2.YkscWA.Tu_qd8U8ItanmCmhhRxDFUoSsyU')
