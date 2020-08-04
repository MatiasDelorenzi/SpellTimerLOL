from riotwatcher import LolWatcher, ApiError
import json

api_key = "RGAPI-6cb5dcab-5382-476f-8c6b-1f04c4b449ef"
watcher = LolWatcher(api_key)
my_region = 'la2'
my_summoner_name = 'EzeXpower'

#Get every spell in the array
with open('spell.json') as f:
    all_spells = json.load(f)

spellsDB = all_spells['data']

barrier = spellsDB['SummonerBarrier']
cleanse = spellsDB['SummonerBoost']
ignite = spellsDB['SummonerDot']
exhaust = spellsDB['SummonerExhaust']
flash = spellsDB['SummonerFlash']
ghost = spellsDB['SummonerHaste']
heal = spellsDB['SummonerHeal']
clarity = spellsDB['SummonerMana']
smite = spellsDB['SummonerSmite']
mark = spellsDB['SummonerSnowball']
teleport = spellsDB['SummonerTeleport']

every_spell = [flash, ignite, teleport, exhaust, heal, smite, barrier, cleanse, ghost, clarity,mark ]

#Get searched player
player = watcher.summoner.by_name(my_region, my_summoner_name)
encrypted_summoner = player['id']
#Get actual game
current_game = watcher.spectator.by_summoner(my_region, encrypted_summoner)
#Get every player in an array
participants = current_game['participants']

#Returns spell name. Input = spell key (INTEGER)
def get_summoner(key):
   k = str(key)
   for x in every_spell:
        if x['key'] == k:
            return x['name']
            break














