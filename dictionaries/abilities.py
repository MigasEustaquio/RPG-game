#https://www.ign.com/wikis/kingdom-hearts-hd-15-remix/Abilities

# (Ability name): [description, AP cost]

abilityList = {

                'Aerial Sweep' : ['Quickly strikes the enemy multiple times in a spiral', 0],               ####
                'Ars Arcanum' : ['?', 0],                                                               ########incomplete
                'Berserk' : ['Boosts attack power when HP is critically low', 0],                           ####
                'Blitz' : ['Quickly attacks the enemy causing critical damage', 0],                         ####
                'Combo Master' : ['Can use magic in combos without losing the finish count', 0],            ####
                'Counterattack' : ['Attacks right after being blocked does more damage', 0],                ####
                'Counter Replenisher' : ['Recover some lost MP when using Counterattack(Required*)', 0],    ####
                'Discharge' : ['Unleashes the keyblade\'s ability that may cause various effects', 0],      ####
                'Finishing Plus' : ['Allows to use a bonus combo finisher', 0],                             ####
                'Gravity Break' : ['Deal strong downward strike while casting the Gravity spell', 0],       ####
                'Hurricane Blast' : ['Rapidly strikes with a powerfull slash causing random damage', 0],    ####
                'Jackpot' : ['Receive more munny in battle', 2],                                            ####
                'Leaf Bracer' : ['Stop enemies from breaking Cure being cast', 1],                          ####
                'Lucky Strike' : ['Raises luck so that enemies drop rare items more often', 3],             ####
                'Mp Haste' : ['more chance to recover MP after battle', 0],                                 ####
                'Mp Rage' : ['recover more MP after battle', 0],                                            ####
                'Negative Combo' : ['Takes 1 hit less to activate a finish', 0],                            ####
                'Ragnarok' : ['?', 0],                                                                  ########incomplete
                'Ripple Drive' : ['Unleashes a powerful blast that deals magical damage', 0],               ####
                'Scan' : ['Display target\'s HP', 1],                                                       ####
                'Second Chance' : ['Ensures to keep 1 HP after taking a critical hit', 0],                  ####         
                'Slapshot' : ['Rapidly strike the enemy. This attacks goes faster than any other.', 0],     ####
                'Sliding Dash' : ['?', 0],                                                                  #
                'Stun Impact' : ['Create a stunning area preventing the enemy from attacking', 0],          ####
                'Sonic Blade':['Slash an enemy while rushing past. Select followup attack for a combo.',0], ####
                'Strike Raid' : ['?', 0],                                                               ########incomplete
                'Trinity Limit': ['?', 0],                                                              ########incomplete
                'Vortex' : ['You strike in a vortex possibly parrying enemies attacks', 0],                 ####
                'Zantetsuken' : ['Focus all the strenght to attack causing massive damage', 0],             ####

}

finishersList = ['Blitz', 'Discharge', 'Gravity Break', 'Hurricane Blast', 'Ripple Drive', 'Stun Impact', 'Zantetsuken']

comboModifiersList = ['Aerial Sweep', 'Slapshot', 'Sliding Dash', 'Vortex']

activeAbilitiesList = ['Ars Arcanum', 'Sonic Blade', 'Strike Raid', 'Ragnarok', 'Trinity Limit']

activeAbilitiesSimple = ['ars arcanum', 'sonic blade', 'strike raid', 'ragnarok', 'trinity limit', 'ars', 'arcanum', 'sonic', 'blade', 'strike', 'raid', 'ragnarok', 'trinity', 'limit']

activeAbilitiesCommands = ['bash','finish','rave','blast','raid','judgment','impact','light']

activeAbilities = {

    'Ars Arcanum' : {'speech':['test'],
                        'MP': 1, 'damage': 1, 'duration': 3, 'final damage': 2,
                        'commands': ['bash','finish']},

    'Sonic Blade' : {'speech':['test'],
                        'MP': 1, 'damage': 1, 'duration': 2, 'final damage': 2,
                        'commands': ['rave','blast']},

    'Strike Raid' : {'speech':['test'],
                        'MP': 1, 'damage': 1, 'duration': 2, 'final damage': 2,
                        'commands': ['raid','judgment']},

    'Ragnarok' : {'speech':['test'],
                        'MP': 1, 'damage': 1, 'duration': 1, 'final damage': 2,
                        'commands': ['impact','impact']},

    'Trinity Limit' : {'speech':['test'],
                        'MP': 1, 'damage': 5, 'duration': 0, 'final damage': 5,
                        'commands': ['light','light']},
}