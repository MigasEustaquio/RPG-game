people = {

            'Leon' : {'speech' : 'Leon: Donald & Goofy are in the Third District!',
                      'reward' : 'key item',
                      'key item': 'Leon\'s tip'
            },
            'Yuffie' : {'speech' : 'Yuffie: Hi there, Sora!\nDid you know that there\'s a shop in the Fisrt District?\n Try typing \'enter shop\'',
                        'reward' : 'key item',
                        'key item' : 'First District Shop location'
            },
            'Moogle' : {'speech' : 'Moogle: Hi there, Kupo!\nTo buy an item just type \'buy [item]\'\n\nHere\'s what I have in stock:',
                        'reward' : 'no'
            },

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

shops = {

            'First District Shop' : {'potion' : 10,
                      'hi-potion' : 20,
                      'ether': 15
            },

}