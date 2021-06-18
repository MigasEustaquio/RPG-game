items = {

                'potion' :{ 'speech':['You healed ', '2 ♥', ' !'],
                        'HP' : 2, 'MP' : 0 },
                'hi-potion' : { 'speech':['You healed ', '3 ♥', ' !'],
                        'HP' : 3, 'MP' : 0 },
                'mega-potion' : { 'speech':['You healed ', '10 ♥', ' !'],
                        'HP' : 10, 'MP' : 0 },
                'ether' : { 'speech':['You restored ', '2 ●', ' !'],
                        'HP' : 0, 'MP' : 2 },
                'hi-ether' : { 'speech':['You restored ', '3 ●', ' !'],
                        'HP' : 0, 'MP' : 3 },
                'mega-ether' : { 'speech':['You restored ', '10 ●', ' !'],
                        'HP' : 0, 'MP' : 10 },
                'elixir' :{ 'speech':['You healed ', '5 ♥', ' and restored ', '5 ●', ' !'],
                        'HP' : 5, 'MP' : 5 },
                'megalixir' : { 'speech':['You healed ', '10 ♥', ' and restored ', '10 ●', ' !'],
                        'HP' : 10, 'MP' : 10 },

}

magics = {

                'fire' :{ 'speech': ['You cast Fire and deal ', '1 ♥', ' of damage!\nThe enemy is now ', 'Burning', 'RED'],
                        'MP' : 1, 'damage' : 1, 'heal' : 0,
                        'status' : {'name': 'Burning', 'speech': ['The enemy is ', 'burning', ' and takes ', '1 ♥', ' of damage!'], 'damage' : 1, 'duration' : 2}
                        },

                'fira' :{ 'speech': ['You cast Fira and deal ', '2 ♥', ' of damage!\nThe enemy is now ', 'Burning', 'RED'],
                        'MP' : 2, 'damage' : 2, 'heal' : 0,
                        'status' : {'name': 'Burning', 'speech': ['The enemy is ', 'burning', ' and takes ', '2 ♥', ' of damage!'], 'damage' : 2, 'duration' : 3}
                        },
                
                'firaga' :{ 'speech': ['You cast Firaga and deal ', '3 ♥', ' of damage!\nThe enemy is now ', 'Burning', 'RED'],
                        'MP' : 3, 'damage' : 3, 'heal' : 0,
                        'status' : {'name': 'Burning', 'speech': ['The enemy is ', 'burning', ' and takes ', '3 ♥', ' of damage!'], 'damage' : 3, 'duration' : 4}
                        },



                'blizzard' : { 'speech' : ['You cast Blizzard and deal ', '1 ♥',  ' of damage!\nThe enemy is now ', 'Freezing', 'BLUE'],
                        'MP' : 1, 'damage' : 1, 'heal' : 0,
                        'status' : {'name': 'Freezing', 'speech': ['The enemy is ','freezing',' and inflicts ','1 ♥',' less of damage!'], 'damage' : 0, 'duration' : 2, 'reduction' : 1}
                        },

                'blizzara' : { 'speech' : ['You cast Blizzara and deal ', '1 ♥',  ' of damage!\nThe enemy is now ', 'Freezing', 'BLUE'],
                        'MP' : 2, 'damage' : 1, 'heal' : 0,
                        'status' : {'name': 'Freezing', 'speech': ['The enemy is ','freezing',' and inflicts ','2 ♥',' less of damage!'], 'damage' : 0, 'duration' : 3, 'reduction' : 2}
                        },

                'blizzaga' : { 'speech' : ['You cast Blizzaga and deal ', '2 ♥',  ' of damage!\nThe enemy is now ', 'Freezing', 'BLUE'],
                        'MP' : 3, 'damage' : 2, 'heal' : 0,
                        'status' : {'name': 'Freezing', 'speech': ['The enemy is ','freezing',' and inflicts ','2 ♥',' less of damage!'], 'damage' : 0, 'duration' : 4, 'reduction' : 2}
                        },



                'thunder' : { 'speech' : ['You cast Thunder and deal ', '2 ♥',  ' of damage!\nThe enemy is now ', 'Paralized', 'YELLOW'],
                        'MP' : 1, 'damage' : 2, 'heal' : 0,
                        'status' : {'name': 'Paralized', 'speech': ['The enemy is ','paralized',' and inflicts ','1 ♥',' less of damage!'], 'damage' : 0, 'duration' : 2, 'reduction' : 1}
                        },

                'thundara' : { 'speech' : ['You cast Thundara and deal ', '4 ♥',  ' of damage!\nThe enemy is now ', 'Paralized', 'YELLOW'],
                        'MP' : 2, 'damage' : 4, 'heal' : 0,
                        'status' : {'name': 'Paralized', 'speech': ['The enemy is ','paralized',' and inflicts ','1 ♥',' less of damage!'], 'damage' : 0, 'duration' : 2, 'reduction' : 1}
                        },

                'thundaga' : { 'speech' : ['You cast Thundaga and deal ', '6 ♥',  ' of damage!\nThe enemy is now ', 'Paralized', 'YELLOW'],
                        'MP' : 3, 'damage' : 6, 'heal' : 0,
                        'status' : {'name': 'Paralized', 'speech': ['The enemy is ','paralized',' and inflicts ','2 ♥',' less of damage!'], 'damage' : 0, 'duration' : 3, 'reduction' : 2}
                        },



                'cure' : { 'speech' : ['You cast Cura and restore ', '3 ♥', ' !'],
                        'MP' : 1, 'damage' : 0, 'heal' : 3,
                         },

                'cura' : { 'speech' : ['You cast Curaga and restore ', '5 ♥', ' !'],
                        'MP' : 2, 'damage' : 0, 'heal' : 5,
                         },

                'curaga' : { 'speech' : ['You cast Cure and restore ', '10 ♥', ' !'],
                        'MP' : 3, 'damage' : 0, 'heal' : 10,
                         },

}

shops = {

            'First District Shop' : {'potion' : 10,
                      'hi-potion' : 20,
                      'ether': 15,
                      'obsidian ring' : 1000
            },





            '1st Floor Shop' : {'potion' : 10,
                      'hi-potion' : 20,
                      'ether': 15,
                      'obsidian ring' : 1000
            },

}


keybladeStatus = { 

            'Kingdom Key' : {
                    'damage' : 1, 
                    'MP': 1 
            },

            'Jungle King' : {
                    'damage' : 2, 
                    'MP': 2 
            },

            'Oathkeeper' : {
                    'damage' : 5, 
                    'MP': 5 
            },

            'Oblivion' : {
                    'damage' : 6, 
                    'MP': 2 
            },

            'Ultima Weapon' : {
                    'damage' : 6, 
                    'MP': 4 
            },
}

equipments = {

        'angel bangle' : {'description' : 'Raises max HP and Defense.',
                        'HP' : 6, 'MP' : 0, 'STR' : 0, 'DEF' : 2},

        'atlas armlet' : {'description' : 'Raises max MP and Defense. Also significantly enhances magic and summon power..',
                        'HP' : 0, 'MP' : 2, 'STR' : 0, 'DEF' : 2},

        'brave warrior' : {'description' : 'Slightly raises max HP and Strength.',
                        'HP' : 3, 'MP' : 0, 'STR' : 1, 'DEF' : 0},

        'cosmic arts' : {'description' : 'Raises max HP and MP.',
                        'HP' : 9, 'MP' : 2, 'STR' : 0, 'DEF' : 2},

        'exp bracelet' : {'description' : 'Increases the experience you get by 20%.',
                        'HP' : 0, 'MP' : 0, 'STR' : -2, 'DEF' : -2},

        'exp earring' : {'description' : 'Increases the experience you get by 20%.',
                        'HP' : 0, 'MP' : 0, 'STR' : 0, 'DEF' : 0},

        'gaia bangle' : {'description' : 'Significantly raises max HP and Defense.',
                        'HP' : 9, 'MP' : 0, 'STR' : 0, 'DEF' : 3},

        'golem chain' : {'description' : 'Raises Strength and Defense.',
                        'HP' : 0, 'MP' : 0, 'STR' : 3, 'DEF' : 1},

        'obsidian ring' : {'description' : 'Raises max HP and Defense.',
                        'HP' : 0, 'MP' : 0, 'STR' : 1, 'DEF' : 0},

        'Omega Arts' : {'description' : 'Raises max HP, Strength, and Defense.',
                        'HP' : 3, 'MP' : 0, 'STR' : 3, 'DEF' : 3},

        'Power Chain' : {'description' : 'Slightly raises Strength.',
                        'HP' : 0, 'MP' : 0, 'STR' : 1, 'DEF' : 0},

        'Prime Cap' : {'description' : 'Raises Defense.',
                        'HP' : 0, 'MP' : 0, 'STR' : -5, 'DEF' : 5},

        'Protect Chain' : {'description' : 'Slightly raises Defense.',
                        'HP' : 0, 'MP' : 0, 'STR' : 0, 'DEF' : 1},

        'Protega Chain' : {'description' : 'Significantly raises Defense.',
                        'HP' : 0, 'MP' : 0, 'STR' : 0, 'DEF' : 3},

        'Protera Chain' : {'description' : 'Raises Defense.',
                        'HP' : 0, 'MP' : 0, 'STR' : 0, 'DEF' : 2},

        'Titan Chain' : {'description' : 'Significantly raises Strength and Defense.',
                        'HP' : 0, 'MP' : 0, 'STR' : 4, 'DEF' : 2},

        
}