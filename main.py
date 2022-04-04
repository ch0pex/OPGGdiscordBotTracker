import discord
import cassiopeia as cass

client = discord.Client()
cass.set_riot_api_key('RGAPI-ea8329f0-1f2d-465d-81cc-63977e5cbc11')

@client.event
async def on_ready():
    print('We gave logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$current'):

        summoner = cass.get_summoner(name=message.content[9:], region='EUW')
        participants = summoner.current_match.to_dict()['participants']
        string_summs = ''
        for i in participants:
            string_summs = string_summs + str(i['summonerName']) + "\n\n"

        av = discord.Embed(title = "Partida en curso: ", color = 7419530, description= string_summs)
        await message.channel.send(embed=av)

client.run('OTYwNTc2MjQ3NDA5Mjk5NTE2.YkscWA.Tu_qd8U8ItanmCmhhRxDFUoSsyU')



