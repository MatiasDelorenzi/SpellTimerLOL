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


def get_spell(name):
    img = ""

    if name == "Flash":
        img = "Flash.png"
    else:
        if name == "Teleport":
            img = "Teleport.png"
        else:
            if name == "Ignite":
                img = "Ignite.png"
            else:
                if name == "Smite":
                    img = "Smite.png"
                else:
                    if name == "Heal":
                        img = "Heal.png"
                    else:
                        if name == "Cleanse":
                            img = "Cleanse.png"
                        else:
                            if name == "Exhaust":
                                img = "Exhaust.png"
                            else:
                                if name == "Ghost":
                                    img = "Ghost.png"
                                else:
                                    if name == "Barrier":
                                        img = "Barrier.png"
                                    else:
                                        if name == "Clarity":
                                            img = "Clarity.png"
                                        else:
                                            img = "Mark.png"
    return img
