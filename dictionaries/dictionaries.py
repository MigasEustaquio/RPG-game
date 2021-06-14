people = {

            'Leon' : {'speech' : 'Leon: Donald & Goofy are in the Third District!',
                      'reward' : 'story',
                      'story' : 1,
                      'mapUpdate' : 'leon '
            },
            'Yuffie' : {'speech' : 'Yuffie: Hi there, Sora!\nDid you know that there\'s a shop in the Fisrt District?\n Try typing \'enter shop\'',
                        'reward' : 'key item',
                        'key item' : 'First District Shop location',
                        'mapUpdate' : 'yuffie '
            },
            'Moogle' : {'speech' : 'Moogle: Hi there, Kupo!\nTo buy an item just type \'buy [item]\'\n\nHere\'s what I have in stock:',
                        'reward' : 'no',
                        'mapUpdate' : 'moogle '
            },

}

maps = {

            'TraverseTown' : {
                    '' : 0,
                    'yuffie ' : 1,
                    'yuffie moogle ' : 2,
                    'leon ' : 3,
                    'yuffie leon ' : 4,
                    'leon yuffie ' : 4,
                    'leon yuffie moogle ' : 5,
                    'yuffie leon moogle ' : 5,
                    'yuffie moogle leon ' : 5,
                    
            },
            'Wonderland' : 0
            
            
}

heartless = {

            'shadow' : {'commands' : 'attack', 
                    'HP': 1 , 'damage': 1,
                    'munny' : [1,5]
            },

            'soldier' : {'commands' : 'attack', 
                    'HP': 2 , 'damage': 1,
                    'munny' : [2,6]
            }
}

items = {

                'potion' :{ 'speech':'You healed 2 ♥ !',
                        'HP' : 2, 'MP' : 0 },
                'hi-potion' : { 'speech':'You healed 3 ♥ !',
                        'HP' : 3, 'MP' : 0 },
                'mega-potion' : { 'speech':'You healed 10 ♥ !',
                        'HP' : 10, 'MP' : 0 },
                'ether' : { 'speech':'You restored 2 ● !',
                        'HP' : 0, 'MP' : 2 },
                'hi-ether' : { 'speech':'You restored 3 ● !',
                        'HP' : 0, 'MP' : 3 },
                'mega-ether' : { 'speech':'You restored 10 ● !',
                        'HP' : 0, 'MP' : 10 },
                'elixir' :{ 'speech':'You healed 5 ♥ and restored 5 ● !',
                        'HP' : 5, 'MP' : 5 },
                'megalixir' : { 'speech':'You healed 10 ♥ and restored 10 ● !',
                        'HP' : 10, 'MP' : 10 },

}

magics = {

                'fire' :{ 'speech': 'You cast Fire and deal 1 ♥ of damage!\nThe enemy is now Burning!',
                        'MP' : 1, 'damage' : 1, 'heal' : 0,
                        'status' : {'speech': 'The enemy is burning and takes 1 ♥ of damage!', 'damage' : 1, 'duration' : 2}
                        },

                'blizzard' : { 'speech' : 'You cast Blizzard and deal 1 ♥ of damage!\nThe enemy is now Freezing!',
                        'MP' : 1, 'damage' : 1, 'heal' : 0,
                        'status' : {'speech': 'The enemy is freezing and inflicts 1 ♥ less of damage!', 'damage' : 0, 'duration' : 2}
                        },
                'cure' : { 'speech' : 'You cast Cure and restore 3 ♥ !',
                        'MP' : 1 },

}

shops = {

            'First District Shop' : {'potion' : 10,
                      'hi-potion' : 20,
                      'ether': 15
            },

}

wordMaps = {

            'TraverseTown' : '',
            'Wonderland' : ''
            }

