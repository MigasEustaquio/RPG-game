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

                'blizzard' : { 'speech' : ['You cast Blizzard and deal ', '1 ♥',  ' of damage!\nThe enemy is now ', 'Freezing', 'BLUE'],
                        'MP' : 1, 'damage' : 1, 'heal' : 0,
                        'status' : {'name': 'Freezing', 'speech': ['The enemy is ','freezing',' and inflicts ','1 ♥',' less of damage!'], 'damage' : 0, 'duration' : 2}
                        },

                'cure' : { 'speech' : ['You cast Cure and restore ', '3 ♥', ' !'],
                        'MP' : 1, 'damage' : 0, 'heal' : 3,
                         },

}

shops = {

            'First District Shop' : {'potion' : 10,
                      'hi-potion' : 20,
                      'ether': 15
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
}