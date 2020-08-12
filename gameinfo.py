import json

with open('spell.json') as f:
    all_spells = json.load(f)


def get_server(name):
    if name == 'Latin America South':
        return 'la2'
    elif name == 'Latin America North':
        return 'la1'
    elif name == 'Brazil':
        return 'br1'
    elif name == 'Europe West':
        return 'euw1'
    elif name == 'Europe Nordic & East':
        return 'eun1'
    elif name == 'North America':
        return 'na1'
    elif name == 'Japan':
        return 'jp1'
    elif name == 'Korea':
        return 'kr'
    elif name == 'Turkey':
        return 'tr1'
    elif name == 'Russia':
        return 'ru'
    elif name == 'Oceania':
        return 'oc1'


def get_cd(name):
    if name == "Flash":
        return "300"
    elif name == "Teleport":
        return "420"
    elif name == "Ignite":
        return "180"
    elif name == "Smite":
        return "90"
    elif name == "Heal":
        return "240"
    elif name == "Cleanse":
        return "210"
    elif name == "Exhaust":
        return "210"
    elif name == "Ghost":
        return "210"
    elif name == "Barrier":
        return "180"
    elif name == "Clarity":
        return "240"
    elif name == "Mark":
        return "80"


def get_spell_image(name):
    # Maybe return Image, Image blurred and cd in an array [Image, Blurred, cd]
    if name == "Flash":
        return "./spells/Flash.png"
    elif name == "Teleport":
        return "./spells/Teleport.png"
    elif name == "Ignite":
        return "./spells/Ignite.png"
    elif name == "Smite":
        return "./spells/Smite.png"
    elif name == "Heal":
        return "./spells/Heal.png"
    elif name == "Cleanse":
        return "./spells/Cleanse.png"
    elif name == "Exhaust":
        return "./spells/Exhaust.png"
    elif name == "Ghost":
        return "./spells/Ghost.png"
    elif name == "Barrier":
        return "./spells/Barrier.png"
    elif name == "Clarity":
        return "./spells/Clarity.png"
    elif name == "Mark":
        return "./spells/Mark.png"


def get_champion_image(name):
    result = "./champions/" + name + ".png"
    return result
