'''from riotwatcher import LolWatcher, ApiError

lol_watcher = LolWatcher('RGAPI-ea8329f0-1f2d-465d-81cc-63977e5cbc11')
my_region = 'euw1'
lol_watcher = LolWatcher('RGAPI-ea8329f0-1f2d-465d-81cc-63977e5cbc11')
me = lol_watcher.summoner.by_name(my_region, 'Ch0pe')
print(me)
my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
game = lol_watcher.
current_game = lol_watcher.spectator.
print(current_game)'''
import cassiopeia
import cassiopeia as cass

cass.set_riot_api_key('RGAPI-ea8329f0-1f2d-465d-81cc-63977e5cbc11')
summoner = cass.get_summoner(name='Ragonflame', region= 'EUW')
print("{name} is a level {level} summoner on the {region} server.".format(name=summoner.name,
                                                                          level=summoner.level,
                                                                          region=summoner.region))

match = summoner.current_match.to_dict()
print(match)

{


"""@client.event
async def on_user_update(before, after):
    guild = await client.fetch_guild(687768751499771929)
    member = guild.get_member(after.id)
    for guild in client.guilds:
        for member in guild.members:
            if member.id == after.id:


        # do stuff
'''    else:
        await message.channel.send('Este usuario no está en partida')'''
"""


"""def current_league_game(summ,message):
    summoner = cass.get_summoner(name = summ, region='EUW')

    participants = summoner.current_match.to_dict()['participants']
    message_participants(participants,message)
"""

"""async def message_participants(dict,message):
    for i in dict:
        await message.channel.send(str(i['summonerName']) + "\n")"""

