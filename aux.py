import cassiopeia as cass
import discord

REGIONS = ['EUW','EUNE','BR','JP', 'KR', 'LAN','LAS','NA','OCE','RU','TR']


async def message_checker(message):
    if "-" in message.content:
        region = message.content.split("-")[1]
        if region not in REGIONS:
            regions_str = 'Region introducida no valida, prueba con:\n'
            for i in REGIONS:
                regions_str += i + "\n"
            return await message.channel.send(regions_str);
    else:
        return REGIONS[0]



async def summoner_checker(message,summoner):
    if summoner.exists is False:
        return await message.channel.send(f'El usuario "{summoner.name}" no existe :(')
    try:
        summoner.current_match
    except:
        await message.channel.send(f'{summoner.name} no esta en partida ahora mismo -.-')
        return False



async def message_embed(message,title,color=7419530,file_name=None,description=""):
    av2 = discord.Embed(title=title, description=description, color=color)
    if file_name:
        file = discord.File(f"/home/acbsu/screenshots/{file_name}", filename=file_name)
        av2.set_image(url=f"attachment://{file_name}")
        return await message.channel.send(file=file, embed=av2)
    return await message.channel.send(embed=av2)
