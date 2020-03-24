from nba_api.stats.static import players
from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import teams


players_list = []


def get_player_info(name):
    player_in = players.find_players_by_full_name(name)
    player_stats = commonplayerinfo.CommonPlayerInfo(player_in[0]['id']).player_headline_stats
    players_list.append('Name: ' + player_in[0]['full_name'])
    players_list.append('Year: ' + player_stats.get_dict()['data'][0][2]
                        + ', PPG: ' + str(player_stats.get_dict()['data'][0][3])
                        + ', APG: ' + str(player_stats.get_dict()['data'][0][4]) +
                        ', RPG: ' + str(player_stats.get_dict()['data'][0][5])
                        + ', PIE: '  + str(player_stats.get_dict()['data'][0][6])
                        )


get_player_info('james harden')


print(players_list)










