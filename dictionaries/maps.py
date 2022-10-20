#Usage: maps [world] [map number(given by the room)] [completion(if the player has details or not)]
maps = {

            'DestinyIslands' : {
                    '1' : {'incomplete' : '10', 'complete' : '11'},
                    
            },        

            'TraverseTown' : {
                    '1' : {'incomplete' : '10', 'complete' : '11'},
                    '2' : {'incomplete' : '20', 'complete' : '21'},
                    
            },
            'Wonderland' : {},


            'OlympusColiseum' : {
                    '1' : {'incomplete' : '10', 'complete' : '11'},
            },


            'CastleOblivion' : {
                    '1' : {'incomplete' : '10', 'complete' : '11'},
            }
            
            
}

#This dict represents the starting maps owned by the player, by default the first map is "incomplete" and the others are "no"
worldMaps = {

            'DestinyIslands' : {'1': 'incomplete'},
            'TraverseTown' : {'1': 'no',
                              '2': 'no'},
            'Wonderland' : {'1': 'no'},
            'DeepJungle' : {'1': 'no'},
            'Atlantica' : {'1': 'no'},
            'OlympusColiseum' : {'1': 'no'},
            'Agrabah' : {'1': 'no'},
            'Monstro' : {'1': 'no'},
            '100AcreWood' : {'1': 'no'},
            'HalloweenTown' : {'1': 'no'},
            'Neverland' : {'1': 'no'},
            'HollowBastion' : {'1': 'no'},
            'EndOfTheWorld' : {'1': 'no'},
            }

#Names to refer to each world on world map screen
worldNames = {

        'DestinyIslands' : ['destiny', 'destiny islands', 'destinyislands'],
        'TraverseTown' : ['traverse', 'traverse town', 'traversetown'],
        'Wonderland' : ['wonder', 'wonderland'],
        'DeepJungle' : ['deep', 'jungle', 'deep jungle', 'deepjungle'],
        'Atlantica' : ['atlantica', 'atlântica'],
        'OlympusColiseum' : ['olympus', 'coliseum', 'olympus coliseum', 'olympuscoliseum'],
        'Agrabah' : ['agrabah', 'agraba'],
        'Monstro' : ['monstro'],
        '100AcreWood' : ['100', 'acre', 'wood', '100 acre', '100 wood', 'acre wood', '100 acre wood'],
        'HalloweenTown' : ['holloween', 'holloween town', 'holloweentown'],
        'Neverland' : ['never', 'neverland'],
        'HollowBastion' : ['hollow', 'bastion', 'hollow bastion', 'hollowbastion'],
        'EndOfTheWorld' : ['end', 'of', 'the', 'world', 'end of the world', 'endoftheworld'],
        'CastleOblivion' : ['castle', 'oblivion', 'castleoblivion', 'castle oblivion']

}

#Simple display name for each world
worldDisplayName = {

        'DestinyIslands' : 'Destiny Islands',
        'TraverseTown' : 'Traverse Town',
        'Wonderland' : 'Wonderland',
        'DeepJungle' : 'Deep Jungle',
        'Atlantica' : 'Atlantica',
        'OlympusColiseum' : 'Olympus Coliseum',
        'Agrabah' : 'Agrabah',
        'Monstro' : 'Monstro',
        '100AcreWood' : '100 Acre Wood',
        'HalloweenTown' : 'Halloween Town',
        'Neverland' : 'Neverland',
        'HollowBastion' : 'Hollow Bastion',
        'EndOfTheWorld' : 'End Of The World',
        'CastleOblivion' : 'Castle Oblivion'


}

worlds = {

        'DestinyIslands' : [],
        'TraverseTown' : [],
        'Wonderland' : [],
        'DeepJungle' : [],
        'Atlantica' : [],
        'OlympusColiseum' : [],
        'Agrabah' : [],
        'Monstro' : [],
        '100AcreWood' : [],
        'HalloweenTown' : [],
        'Neverland' : [],
        'HollowBastion' : [],
        'EndOfTheWorld' : [],
        'CastleOblivion' : []

}