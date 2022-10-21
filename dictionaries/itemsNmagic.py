items = {

                'potion' :{ 'speech':['You healed ', '2 ♥', ' !'],
                        'HP' : 2, 'MP' : 0 },
                'hi-potion' : { 'speech':['You healed ', '3 ♥', ' !'],
                        'HP' : 3, 'MP' : 0 },
                'mega-potion' : { 'speech':['You healed ', '10 ♥', ' !'],
                        'HP' : 10, 'MP' : 0 },
                'ether' : { 'speech':['You restored ', '2 ●', ' !'],
                        'HP' : 0, 'MP' : 2 },
                'hi-ether' : { 'speech':['You restored ', '4 ●', ' !'],
                        'HP' : 0, 'MP' : 4 },
                'mega-ether' : { 'speech':['You restored ', '10 ●', ' !'],
                        'HP' : 0, 'MP' : 10 },
                'elixir' :{ 'speech':['You healed ', '5 ♥', ' and restored ', '5 ●', ' !'],
                        'HP' : 5, 'MP' : 5 },
                'megalixir' : { 'speech':['You healed ', '10 ♥', ' and restored ', '10 ●', ' !'],
                        'HP' : 10, 'MP' : 10 },

}

magics = {

                'fire' :{ 'speech': ['You cast Fire and deal ', ' ♥', ' of damage!\nThe enemy is now ', 'Burning', 'RED'],
                        'MP' : 1, 'damage' : 1, 'heal' : 0,
                        'status' : {'name': 'Burning', 'speech': ['The enemy is ', 'burning', ' and takes ', '1 ♥', ' of damage!'], 'damage' : 1, 'duration' : 2, 'reduction' : 0}
                        },

                'fira' :{ 'speech': ['You cast Fira and deal ', ' ♥', ' of damage!\nThe enemy is now ', 'Burning', 'RED'],
                        'MP' : 2, 'damage' : 2, 'heal' : 0,
                        'status' : {'name': 'Burning', 'speech': ['The enemy is ', 'burning', ' and takes ', '2 ♥', ' of damage!'], 'damage' : 2, 'duration' : 3, 'reduction' : 0}
                        },
                
                'firaga' :{ 'speech': ['You cast Firaga and deal ', ' ♥', ' of damage!\nThe enemy is now ', 'Burning', 'RED'],
                        'MP' : 3, 'damage' : 3, 'heal' : 0,
                        'status' : {'name': 'Burning', 'speech': ['The enemy is ', 'burning', ' and takes ', '3 ♥', ' of damage!'], 'damage' : 3, 'duration' : 4, 'reduction' : 0}
                        },



                'blizzard' : { 'speech' : ['You cast Blizzard and deal ', ' ♥',  ' of damage!\nThe enemy is now ', 'Freezing', 'BLUE'],
                        'MP' : 1, 'damage' : 1, 'heal' : 0,
                        'status' : {'name': 'Freezing', 'speech': ['The enemy is ','freezing',' and inflicts ','1 ♥',' less of damage!'], 'damage' : 0, 'duration' : 2, 'reduction' : 1}
                        },

                'blizzara' : { 'speech' : ['You cast Blizzara and deal ', ' ♥',  ' of damage!\nThe enemy is now ', 'Freezing', 'BLUE'],
                        'MP' : 2, 'damage' : 1, 'heal' : 0,
                        'status' : {'name': 'Freezing', 'speech': ['The enemy is ','freezing',' and inflicts ','2 ♥',' less of damage!'], 'damage' : 0, 'duration' : 3, 'reduction' : 2}
                        },

                'blizzaga' : { 'speech' : ['You cast Blizzaga and deal ', ' ♥',  ' of damage!\nThe enemy is now ', 'Freezing', 'BLUE'],
                        'MP' : 3, 'damage' : 2, 'heal' : 0,
                        'status' : {'name': 'Freezing', 'speech': ['The enemy is ','freezing',' and inflicts ','2 ♥',' less of damage!'], 'damage' : 0, 'duration' : 4, 'reduction' : 2}
                        },



                'thunder' : { 'speech' : ['You cast Thunder and deal ', ' ♥',  ' of damage!\nThe enemy is now ', 'Paralized', 'YELLOW'],
                        'MP' : 1, 'damage' : 2, 'heal' : 0,
                        'status' : {'name': 'Paralized', 'speech': ['The enemy is ','paralized',' and inflicts ','1 ♥',' less of damage!'], 'damage' : 0, 'duration' : 2, 'reduction' : 1}
                        },

                'thundara' : { 'speech' : ['You cast Thundara and deal ', ' ♥',  ' of damage!\nThe enemy is now ', 'Paralized', 'YELLOW'],
                        'MP' : 2, 'damage' : 4, 'heal' : 0,
                        'status' : {'name': 'Paralized', 'speech': ['The enemy is ','paralized',' and inflicts ','1 ♥',' less of damage!'], 'damage' : 0, 'duration' : 2, 'reduction' : 1}
                        },

                'thundaga' : { 'speech' : ['You cast Thundaga and deal ', ' ♥',  ' of damage!\nThe enemy is now ', 'Paralized', 'YELLOW'],
                        'MP' : 3, 'damage' : 6, 'heal' : 0,
                        'status' : {'name': 'Paralized', 'speech': ['The enemy is ','paralized',' and inflicts ','2 ♥',' less of damage!'], 'damage' : 0, 'duration' : 3, 'reduction' : 2}
                        },



                'cure' : { 'speech' : ['You cast Cure and restore ', '3 ♥', ' !', '', 'GREEN'],
                        'MP' : 1, 'damage' : 0, 'heal' : 3,
                         },

                'cura' : { 'speech' : ['You cast Cura and restore ', '5 ♥', ' !', '', 'GREEN'],
                        'MP' : 2, 'damage' : 0, 'heal' : 5,
                         },

                'curaga' : { 'speech' : ['You cast Curaga and restore ', '10 ♥', ' !', '', 'GREEN'],
                        'MP' : 3, 'damage' : 0, 'heal' : 10,
                         },

                #damage based on enemy health and player total mp?
                'gravity' : {'speech' : ['', '', '', '', 'BLUE'] , 'status' : {'name': 'gravity', 'speech': ['The ','gravity',' effect makes the enemy too heavy too attack! It inflicts ','0 ♥',' of damage!'], 'damage' : 0, 'duration' : 1, 'reduction' : 1}
                        },

                #defense
                'aero' : {'speech' : ['', '', '', '', 'BLUE'] , 'status' : {'name': 'gravity', 'speech': ['The ','aero',' ','0 ♥',' of damage!'], 'damage' : 0, 'duration' : 1, 'reduction' : 1}
                        },

}


keybladeStatus = { 

            'Kingdom Key' : {
                    'damage' : 1, 
                    'MP': 0 
            },

            'Jungle King' : {
                    'damage' : 3, 
                    'MP': 0 
            },

            'Lady Luck' : {
                    'damage' : 5, 
                    'MP': 2 
            },

            'Olympia' : {
                    'damage' : 8, 
                    'MP': 0 
            },

            'Three Wishes' : {
                    'damage' : 4, 
                    'MP': 0 
            },

            'Wishing Star' : {
                    'damage' : 3, 
                    'MP': 0 
            },

            'Spellbinder' : {
                    'damage' : 2, 
                    'MP': 2 
            },

            'Crabclaw' : {
                    'damage' : 4, 
                    'MP': 1 
            },

            'Pumpkinhead' : {
                    'damage' : 5, 
                    'MP': 0 
            },

            'Fairy Harp' : {
                    'damage' : 8, 
                    'MP': 1 
            },

            'Metal Chocobo' : {
                    'damage' : 7, 
                    'MP': -1 
            },

            'Divine Rose' : {
                    'damage' : 11, 
                    'MP': 0 
            },

            'Lionheart' : {
                    'damage' : 8, 
                    'MP': 1 
            },

            'Diamond Dust' : {
                    'damage' : 1, 
                    'MP': 3 
            },

            'One-Winged Angel' : {
                    'damage' : 6, 
                    'MP': -2 
            },

            'Oathkeeper' : {
                    'damage' : 7, 
                    'MP': 1 
            },

            'Oblivion' : {
                    'damage' : 9, 
                    'MP': -1 
            },

            'Ultima Weapon' : {
                    'damage' : 12, 
                    'MP': 2 
            },

            'Kingdom Key D' : {
                    'damage' : 8, 
                    'MP': 4 
            },

            'Keyblade of heart' : {
                    'damage' : 8, 
                    'MP': 4 
            },
}

equipments = {

        'angel bangle' : {'description' : 'Raises max HP and Defense.',
                        'HP' : 6, 'MP' : 0, 'STR' : 0, 'DEF' : 2, 'AP' : 0},

        'atlas armlet' : {'description' : 'Raises max MP and Defense. Also significantly enhances magic and summon power..',
                        'HP' : 0, 'MP' : 2, 'STR' : 0, 'DEF' : 2, 'AP' : 0},

        'brave warrior' : {'description' : 'Slightly raises max HP and Strength.',
                        'HP' : 3, 'MP' : 0, 'STR' : 1, 'DEF' : 0, 'AP' : 0},

        'cosmic arts' : {'description' : 'Raises max HP and MP.',
                        'HP' : 9, 'MP' : 2, 'STR' : 0, 'DEF' : 2, 'AP' : 0},

        'exp bracelet' : {'description' : 'Increases the experience you get by 20%.',
                        'HP' : 0, 'MP' : 0, 'STR' : -2, 'DEF' : -2, 'AP' : 0},

        'exp earring' : {'description' : 'Increases the experience you get by 20%.',
                        'HP' : 0, 'MP' : 0, 'STR' : 0, 'DEF' : 0, 'AP' : 0},

        'gaia bangle' : {'description' : 'Significantly raises max HP and Defense.',
                        'HP' : 9, 'MP' : 0, 'STR' : 0, 'DEF' : 3, 'AP' : 0},

        'golem chain' : {'description' : 'Raises Strength and Defense.',
                        'HP' : 0, 'MP' : 0, 'STR' : 3, 'DEF' : 1, 'AP' : 0},

        'obsidian ring' : {'description' : 'Raises max HP and Defense.',
                        'HP' : 0, 'MP' : 0, 'STR' : 1, 'DEF' : 0, 'AP' : 0},

        'Omega Arts' : {'description' : 'Raises max HP, Strength, and Defense.',
                        'HP' : 3, 'MP' : 0, 'STR' : 3, 'DEF' : 3, 'AP' : 0},

        'Power Chain' : {'description' : 'Slightly raises Strength.',
                        'HP' : 0, 'MP' : 0, 'STR' : 1, 'DEF' : 0, 'AP' : 0},

        'Prime Cap' : {'description' : 'Raises Defense.',
                        'HP' : 0, 'MP' : 0, 'STR' : -5, 'DEF' : 5, 'AP' : 0},

        'Protect Chain' : {'description' : 'Slightly raises Defense.',
                        'HP' : 0, 'MP' : 0, 'STR' : 0, 'DEF' : 1, 'AP' : 0},

        'Protega Chain' : {'description' : 'Significantly raises Defense.',
                        'HP' : 0, 'MP' : 0, 'STR' : 0, 'DEF' : 3, 'AP' : 0},

        'Protera Chain' : {'description' : 'Raises Defense.',
                        'HP' : 0, 'MP' : 0, 'STR' : 0, 'DEF' : 2, 'AP' : 0},

        'Titan Chain' : {'description' : 'Significantly raises Strength and Defense.',
                        'HP' : 0, 'MP' : 0, 'STR' : 4, 'DEF' : 2, 'AP' : 0},

        
}