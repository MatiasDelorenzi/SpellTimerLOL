from riotwatcher import LolWatcher, ApiError
import json

api_key = "RGAPI-6cb5dcab-5382-476f-8c6b-1f04c4b449ef"
watcher = LolWatcher(api_key)
my_region = 'la2'
my_summoner_name = 'reketed'

#Get every spell in the array
with open('spell.json') as f:
    all_spells = json.load(f)

with open('champion.json') as a:
    all_champions = json.load(a)

#Returns spell name. Input = spell key (INTEGER)
def get_summoner(key):
   k = str(key)
   for s in spell_aux:
        actual = all_spells[s]
        if actual['key'] == k:
            return actual['name']
            break

#Returns champion name. Input = Champion key (INTEGER)
def get_champion(key):
    k = str(key)
    for c in champ_aux:
        actual = all_champions[c]
        if actual['key'] == k:
            return c
            break

spell_aux = ["SummonerBarrier", "SummonerBoost","SummonerDot","SummonerExhaust","SummonerFlash","SummonerHaste","SummonerHeal","SummonerMana","SummonerSmite","SummonerSnowball","SummonerTeleport"]
champ_aux = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe", "AurelionSol", "Azir", "Bard","Blitzcrank","Brand","Braum","Caitlyn", "Camille","Cassiopeia","Chogath","Corki","Darius","Diana","Draven","DrMundo","Ekko","Elise","Evelynn","Ezreal","Fiddlesticks","Fiora","Fizz","Galio","Gangplank","Garen","Gnar","Gragas","Graves","Hecarim","Heimerdinger","Illaoi","Irelia","Ivern","Janna","JarvanIV","Jax","Jayce","Jhin","Jinx","Kaisa","Kalista","Karma","Karthus","Kassadin","Katarina","Kayle","Kayn","Kennen","Khazix","Kindred","Kled","KogMaw","Leblanc","LeeSin","Leona","Lillia","Lissandra","Lucian","Lulu","Lux","Malphite","Malzahar","Maokai","MasterYi","MissFortune","MonkeyKing","Mordekaiser","Morgana","Nami","Nasus","Nautilus","Neeko","Nidalee","Nocturne","Nunu","Olaf","Orianna","Ornn","Pantheon","Poppy","Pyke","Qiyana","Quinn","Rakan","Rammus","RekSai","Renekton","Rengar","Riven","Rumble","Ryze","Sejuani","Senna","Sett","Shaco","Shen","Shyvana","Singed","Sion","Sivir","Skarner","Sona","Swain","Sylas","Syndra","TahmKench","Taliyah","Talon","Taric","Teemo","Thresh","Tristana","Trundle","Tryndamere","TwistedFate","Twitch","Udyr","Urgot","Varus","Vayne","Veigar","Velkoz","Vi","Viktor","Vladimir","Volibear","Warwick","Xayah","Xerath","XinZhao","Yasuo","Yorick","Yuumi","Zac","Zed","Ziggs","Zilean","Zoe","Zyra"]

#Get searched player
player = watcher.summoner.by_name(my_region, my_summoner_name)
encrypted_summoner = player['id']

#Get actual game
current_game = watcher.spectator.by_summoner(my_region, encrypted_summoner)

#Get every player in an array
participants = current_game['participants']

player_one = participants[0]
player_two = participants[1]
player_three = participants[2]
player_four = participants[3]
palyer_five = participants[4]
player_six = participants[5]
player_seven = participants[6]
player_eight = participants[7]
player_nine = participants[8]
player_ten = participants[9]

blue_team_aux = [player_one['summonerName'],player_two['summonerName'],player_three['summonerName'],player_four['summonerName'],palyer_five['summonerName']]
blue_team = [player_one, player_two, player_three, player_four,palyer_five]
red_team = [player_six,player_seven,player_eight,player_nine,player_ten]
is_on_blue = True
enemies = []

if my_summoner_name in blue_team_aux:
    enemies = red_team
else:
    enemies = blue_team

#Enemies is the list where i need to get the spellsID
game_info = []

for i in range(5):
    enemy = enemies[i]
    summoner1 = get_summoner(enemy['spell1Id'])
    summoner2 = get_summoner(enemy['spell2Id'])
    champion = get_champion(enemy['championId'])
    game_info.append([champion, summoner1,summoner2])


print(game_info)










