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

"""[{'teamId': 100, 'spell1Id': 11, 'spell2Id': 4, 'championId': 131, 'profileIconId': 4887, 'summonerName': 'Xantmann', 'bot': False, 'summonerId': '0Sz1-myDmCwa9q9nJJnJNeVqqEV7l9AS5l5LvKbALm29Lo3I', 'gameCustomizationObjects': [], 'perks': {'perkIds': [8010, 9111, 9104, 8014, 8304, 8347, 5005, 5008, 5002], 'perkStyle': 8000, 'perkSubStyle': 8300}},
 {'teamId': 100, 'spell1Id': 14, 'spell2Id': 4, 'championId': 25, 'profileIconId': 3587, 'summonerName': 'MOBINZZZ', 'bot': False, 'summonerId': 'Ejg1XUqzvhfhgxe6OK3BF_4b5ghTsqN1BCj2KMLxeqk6Lhs', 'gameCustomizationObjects': [], 'perks': {'perkIds': [8229, 8226, 8210, 8237, 8313, 8345, 5008, 5008, 5002], 'perkStyle': 8200, 'perkSubStyle': 8300}},
 {'teamId': 100, 'spell1Id': 7, 'spell2Id': 4, 'championId': 51, 'profileIconId': 4887, 'summonerName': 'Giuseppe02', 'bot': False, 'summonerId': 'gCSKI2_Tkr5SelCTnB_TmqL3wHQ4Wrt9g3A13UPiFIxgF4c8', 'gameCustomizationObjects': [], 'perks': {'perkIds': [8021, 8009, 9103, 8014, 8233, 8236, 5005, 5008, 5002], 'perkStyle': 8000, 'perkSubStyle': 8200}},
 {'teamId': 100, 'spell1Id': 4, 'spell2Id': 12, 'championId': 150, 'profileIconId': 503, 'summonerName': 'Sushinchu', 'bot': False, 'summonerId': '9M5nsfF2CIavR-tDpj07wYMaPedQSDlF4STKsGWrfz9YMH0', 'gameCustomizationObjects': [], 'perks': {'perkIds': [8437, 8446, 8473, 8451, 8139, 8135, 5005, 5008, 5002], 'perkStyle': 8400, 'perkSubStyle': 8100}},
 {'teamId': 100, 'spell1Id': 4, 'spell2Id': 14, 'championId': 103, 'profileIconId': 5212, 'summonerName': 'javitovk25', 'bot': False, 'summonerId': '2_nsOMSBKK_XLexCKG13AmhJ3NIXCTkog6sV6IKr-sOZC0M', 'gameCustomizationObjects': [], 'perks': {'perkIds': [8112, 8139, 8138, 8106, 8345, 8352, 5005, 5008, 5003], 'perkStyle': 8100, 'perkSubStyle': 8300}},
 {'teamId': 200, 'spell1Id': 14, 'spell2Id': 4, 'championId': 31, 'profileIconId': 20, 'summonerName': 'Enterman', 'bot': False, 'summonerId': 'Fl3maYuCc-FwPLAGH-DvvT8KuApr7K61FUbT5yfK1iuPCgjN', 'gameCustomizationObjects': [], 'perks': {'perkIds': [9923, 8126, 8138, 8106, 8345, 8410, 5005, 5008, 5003], 'perkStyle': 8100, 'perkSubStyle': 8300}},
 {'teamId': 200, 'spell1Id': 4, 'spell2Id': 11, 'championId': 9, 'profileIconId': 4924, 'summonerName': 'Vinho Rolha', 'bot': False, 'summonerId': 'EJC81Y7BXVCjVLeaMhUV7G7okMrT0zQnN6YeRqume3CPgxBuVjFMjPl8vQ', 'gameCustomizationObjects': [], 'perks': {'perkIds': [8112, 8126, 8138, 8106, 8313, 8347, 5008, 5008, 5002], 'perkStyle': 8100, 'perkSubStyle': 8300}},
 {'teamId': 200, 'spell1Id': 14, 'spell2Id': 4, 'championId': 236, 'profileIconId': 5212, 'summonerName': 'Le roi Banane', 'bot': False, 'summonerId': 't1hHXRatS2thYCr-L1OfXTiqKeUHwoDSR_8hJ9ye8CA4QvQ', 'gameCustomizationObjects': [], 'perks': {'perkIds': [8005, 8009, 9104, 8017, 8304, 8347, 5005, 5008, 5003], 'perkStyle': 8000, 'perkSubStyle': 8300}},
 {'teamId': 200, 'spell1Id': 7, 'spell2Id': 4, 'championId': 21, 'profileIconId': 5021, 'summonerName': 'Chmems', 'bot': False, 'summonerId': 'KJ5ZnlZgEIPQAXoiqQy5J-1te52KO09oavyhHPxLc1dVlA-v7ddpAhPUjg', 'gameCustomizationObjects': [], 'perks': {'perkIds': [8369, 8304, 8345, 8347, 8236, 8275, 5008, 5008, 5002], 'perkStyle': 8300, 'perkSubStyle': 8200}},
 {'teamId': 200, 'spell1Id': 4, 'spell2Id': 14, 'championId': 3, 'profileIconId': 3377, 'summonerName': 'Shakur93', 'bot': False, 'summonerId': '7YnC6t0ZikDWemikKgVi3fzDG283jzsIcvDWah4vp_dXwZidqKnSKEkQWQ', 'gameCustomizationObjects': [], 'perks': {'perkIds': [8439, 8401, 8473, 8242, 8275, 8210, 5008, 5008, 5002], 'perkStyle': 8400, 'perkSubStyle': 8200}}]

"""