#https://www.ign.com/wikis/kingdom-hearts-hd-15-remix/Abilities

# (Ability name): [description, AP cost]

abilityList = {

        'Aerial Sweep' : ['Sora quickly strikes the enemy multiple times in a spiral', 0],
        'Ars Arcanum' : ['Sora unleashes a formidable attack. Select followup attack for a combo', 0],
        'Berserk' : ['Boosts attack power when HP is critically low', 0],
        'Blitz' : ['Sora quickly attacks the enemy causing critical damage', 0],
        'Combo Master' : ['Sora can use magic in combos without losing the finish count', 0],
        'Counterattack' : ['Sora can attack right after being blocked for a powerful strike', 0],
        'Counter Replenisher' : ['Sora recovers some lost MP when using Counterattack (Requires Counterattack)', 0],    #
        'Discharge' : ['Sora unleashes his keyblade\'s special ability. It may cause various effects', 0],              #
        'EXP Boost': ['Increases EXP received by 20%', 0],
        'Finishing Plus' : ['Allows Sora to use a bonus combo finisher', 0],                                            #
        'Gravity Break' : ['Sora deals a strong downward strike while casting the Gravity spell', 0],
        'Hurricane Blast' : ['Sora rapidly strikes with a powerfull slash causing damage that may vary', 0],
        'Jackpot' : ['Receive more munny after battles', 2],
        'Leaf Bracer' : ['grants invulnerability while casting any healing spell', 1],
        'Lucky Strike' : ['Raises luck so that enemies drop rare items more often', 3],
        'Mp Haste' : ['Increases the chance of recovering MP after battles', 0],
        'Mp Rage' : ['Increaases the amount of MP recoverd after battles', 0],
        'Negative Combo' : ['Decreases by 1 the amount of attacks needed to activate a finish', 0],                     #
        'Ragnarok' : ['Sora unleashes a powerful combo followed by a great magical sphere', 0],
        'Ripple Drive' : ['Sora unleashes a powerful blast that deals magical damage to the enemies', 0],
        'Scan' : ['Display target\'s HP', 1],
        'Second Chance' : ['Ensures to keep 1 HP after taking a critical hit', 0],      
        'Slapshot' : ['Sora rapidly strikes the enemy. This attacks goes faster than any other.', 0],
        'Sliding Dash' : ['?', 0],                                                           ###################
        'Stun Impact' : ['Sora creates a stunning area preventing the enemy from attacking', 0],
        'Sonic Blade':['Sora slashs an enemy while rushing past. Select followup attack for a combo.',0],
        'Strike Raid' : ['Sora throws his keyblade against the enemies. Select followup attack for a combo.', 0],
        'Trinity Limit': ['Sora charges a powerful magical wave that crushes the enemies', 0],
        'Vortex' : ['Sora strikes in a vortex possibly parrying enemies attacks', 0],
        'Zantetsuken' : ['Sora focus all his strenght into an attack causing massive damage', 0],

}

# stackAbilities = ['Jackpot', 'Lucky Strike', 'Mp Haste', 'Mp Rage']

finishersList = ['Blitz', 'Discharge', 'Gravity Break', 'Hurricane Blast', 'Ripple Drive', 'Stun Impact', 'Zantetsuken']

comboModifiersList = ['Aerial Sweep', 'Slapshot', 'Sliding Dash', 'Vortex']

activeAbilitiesList = ['Ars Arcanum', 'Sonic Blade', 'Strike Raid', 'Ragnarok', 'Trinity Limit']

activeAbilitiesSimple = ['ars arcanum', 'sonic blade', 'strike raid', 'ragnarok', 'trinity limit', 'ars', 'arcanum', 'sonic', 'blade', 'strike', 'raid', 'ragnarok', 'trinity', 'limit']

activeAbilitiesCommands = ['bash','finish','rave','blast','raid','judgment','impact','light']

activeAbilities = {

    'Ars Arcanum' : {'speech': {'damage': ['\nSora unleashes a flurry of slashes. You deal ','\nSelect followup attack for a combo!'],
                                'final damage': ['\nSora executes a powerful finishing strike. You deal ', '']},
                        'MP': 5, 'damage': 1, 'duration': 3, 'final damage': 2,
                        'commands': ['bash','finish']},

    'Sonic Blade' : {'speech': {'damage': ['\nSora slashes the enemy while rushing past. You deal ','\nSelect followup attack for a combo!'],
                                'final damage': ['\nSora blasts the enemy while rushing past. You deal ','']},
                        'MP': 3, 'damage': 1, 'duration': 2, 'final damage': 2,
                        'commands': ['rave','blast']},

    'Strike Raid' : {'speech': {'damage': ['\nSora throws the keyblade at the enemy. You deal ','\nSelect followup attack for a combo!'],
                                'final damage': ['\nSora throws the keyblade for a powerful final blow. You deal ', '']},
                        'MP': 3, 'damage': 1, 'duration': 2, 'final damage': 2,
                        'commands': ['raid','judgment']},

    'Ragnarok' : {'speech': {'damage': ['\nSora delivers a powerful combo at the enemy and begin charging energy into a magical sphere. You deal ','\nSelect followup attack for a combo!'],
                                'final damage': ['\nSora releases the energy in a series of projectiles that flyes to the enemy. You deal ', '']},
                        'MP': 4, 'damage': 1, 'duration': 1, 'final damage': 2,
                        'commands': ['impact','impact']},

    'Trinity Limit' : {'speech': {'damage': ['\nSora charges all his power into a magical wave of energy that crushes the enemy. You deal ', ''],
                                'final damage': ['\nSora charges all his power into a magical wave of energy that crushes the enemy. You deal ', '']},
                        'MP': 6, 'damage': 5, 'duration': 0, 'final damage': 5,
                        'commands': ['light','light']},
}