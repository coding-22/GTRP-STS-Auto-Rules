from pynput.keyboard import Key, Listener, Controller

keyboard = Controller()

rules = [
    'RDM (Random Deathmatch) is not tolerated. It may result in a ban',
    'VDM (Vehicle Deathmatch) is not tolerated. It may result in a kick.',
    'No suicide RP whatsoever, it is against Roblox TOS.',
    'Once you are shot to half HP (yellow) or lower, you must lay down and Roleplay that you have been shot.',
    'You must RP all crashes.',
    'No cop baiting. Meaning you cannot go and intentionally grab a cop\'s attention.',
    'Avoiding a MOD when they\'re trying to conduct a sit will result in automatic kick',
    'No pointless racing around the map! It’s annoying. This is not a public server.',
    'Do Not cuff rush. You must say “-cuffs-” before actually cuffing the person.',
    'Do not just arrest a suspect at the scene. RP the whole scene and transport them to the Liberty County Jail.',
    'Red police cars and Unmarked corvette are reserved for mods, do not use them!',
    'The LMG (gamepass gun) is banned. Unless you are VIP',
    'No gangs/mafias. This is not allowed due to how out of hand they get. They are also against Roblox TOS.',
    'If you are grouping it will be considered as this.',
    '*this*',
    'No patrolling as SWAT. Do not leave the station unless dispatched or refueling.',
    'No exotics, this includes the corvette. Unless you are VIP',
    'Do not interfere with ongoing RP scenes. It may result into a respawn',
    'You must be in a group of 3, no more or less to conduct jewelry store robbery.',
    'You MUST not run from the police in a vehicle UNLESS you are wanted or have a valid reason to be running',
    'The “new life rule” is in effect. Do not return to a scene once you are dead. You don’t remember anything.',
    '*dead*',
    'Fear RP is enabled. Meaning if someone has a gun pointed towards you, you must comply with his demands.',
    'No kidnapping unless you have a mods permission. It is considered an event. They get too out of hand and way too frequent.',
    'No unrealistic/troll avatars.',
    'Leaving to avoid a punishment is an automatic ban.',
    'Priority cooldowns are in effect after each priority for 5 minutes.',
    'Just use common sense and follow Roblox TOS.'
]

current = 0

def on_press(key):
    print('{0} key pressed'.format(key))

def on_release(key):
    print('{0} key released'.format(key))

    if key == Key.delete:
        # Stop listener
        return False
    

    # Read rules

    global current

    if key == Key.f8:
        keyboard.type('{0}'.format(rules[current]))

        if current == len(rules) - 1:
            current = 0
        else:
            current += 1
    
    if key == Key.f7:
        current = 0

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()