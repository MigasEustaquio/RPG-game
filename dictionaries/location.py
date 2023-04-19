#a dictionary linking a room to other room positions

# The first '0' of each world represents the starting room

# 'map number' : refers to the map image that the room is in
# 'heartless' : (story)
# 'resetHeartless' : what room have their heartless reset upon entering
# 'unlock' : {'magic to unlock(?)':['direction', 'message after unlocking', 'unlock other area', 'direction of the other area']}

rooms = {

  'DestinyIslands': {

    0 : 'Snow White\'s Stained Glass',

      'Snow White\'s Stained Glass' : { 'down' : 'Cinderella\'s Stained Glass',
                  'resetHeartless' : [],
                  'map number' : '0',
                  'restricted' : {},
                  'move': ['down']
      },

      'Cinderella\'s Stained Glass' : { 'down' : 'Unknown',
                  'resetHeartless' : [],
                  'heartless'  : '',
                  'treasure' : '',
                  'map number' : '0',
                  'restricted' : {},
                  'move': ['down']
      },

      'Unknown' : { 'down' : 'Aurora\'s Stained Glass',
                  'resetHeartless' : [],
                  'treasure' : '',
                  'map number' : '0',
                  'restricted' : {},
                  'move': ['down']
      },

      'Aurora\'s Stained Glass' : { 'down' : 'Belle\'s Stained Glass',
                  'resetHeartless' : [],
                  'Save':'',
                  'map number' : '0',
                  'restricted' : {},
                  'move': ['down']
      },

      'Belle\'s Stained Glass' : { 'down' : 'Seashore',
                  'resetHeartless' : [],
                  'heartless'  : '',
                  'map number' : '0',
                  'restricted' : {},
                  'move': ['down']
      },

      'Seashore' : { 'right' : 'Cove',
                  'down' : 'Paopu Tree',
                  'left' : 'Secret Place',
                  'up' : 'Seaside Shack',
                  'person'  : ['Kairi'],
                  'resetHeartless' : [],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['right', 'down', 'left', 'up']
      }, 

      'Cove' : { 'left' : 'Seashore',
                  'up' : 'Seaside Shack',
                  'treasure' : '',
                  'person'  : ['Riku', 'Kairi'],
                  'resetHeartless' : [],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['left', 'up']
      },

      'Seaside Shack' : { 'right' : 'Cove',
                  'down' : 'Seashore',
                  'resetHeartless' : [],
                  'Save':'',
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['right', 'down']
      },

      'Paopu Tree' : { 'up' : 'Seashore',
                  'person'  : ['Riku'],
                  'resetHeartless' : [],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['up']
      },

      'Secret Place' : {'down' : 'Seashore',
                  'right' : 'Seashore',
                  'resetHeartless' : [],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['right', 'down']
      },

      'Rooms List' : {
                  'resetHeartless' : ['Seashore', 'Cove', 'Seaside Shack', 'Paopu Tree', 'Secret Place']
      }

  },

  'TraverseTown' : {

    0 : 'First District',

            'First District' : { 'up' : 'Second District',
                  'right' : 'Third District',
                  'shop' : 'First District Shop',
                  'resetHeartless' : ['Hotel', 'Alleyway'],
                  'map number' : '1',
                  'restricted' : {'right' : 'The door seems to be blocked...'},
                  'move': ['right', 'up']
            },        

            'Second District' : { 'down' : 'First District',
                  'right' : 'Third District',
                  'left' : 'Hotel',
                  'up' : 'Gizmo Shop',
                  'treasure' : '',
                  'heartless'  : '',
                  'resetHeartless' : ['Alleyway', 'Third District Upper Side'],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['right', 'down', 'left', 'up']
                },
                
            'Third District' : { 'down' : 'First District',
                  'left'  : 'Second District',
                  'up' : 'Mystical House',
                  'right' : 'Small House',
                  'resetHeartless' : ['Hotel', 'Alleyway'],
                  'map number' : '1',
                  'restricted' : {'down' : 'The door seems to be blocked...\nThere appears to be some sparkles coming out of a severed power cord near the door...',
                                  'up' : 'There is a black wall with a symbol that resembles fire...',
                  },
                  'unlock' : {'thu':['down', ' and hit the power cord. Some mechanisms inside the door seems to be moving now!', 'First District', 'right'],
                              'fir':['up', ' and the fire symbol on the wall glows red. It opens before you!']
                              },
                  'move': ['right', 'down', 'left', 'up']
                },

            'Small House' : { 'left' : 'Third District',
                  'person'  : ['Leon'],
                  'resetHeartless' : ['Second District'],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['left']
                },

            'Dalmatian House' : { 'leave' : 'Second District',
                  'person'  : ['Pongo'],
                  'resetHeartless' : ['Gizmo Shop', 'Third District', 'Hotel'],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['leave']
                },
                
            'Hotel' : { 'right' : 'Second District',
                    'left' : 'Green Room',
                    'up' : 'Red Room',
                    'heartless'  : '',
                    'resetHeartless' : ['Alleyway'],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['right', 'left', 'up']
             },

             'Green Room' : { 'right' : 'Hotel',
                  'up' : 'Alleyway',
                  'person'  : ['Leon'],
                  'resetHeartless' : ['Second District'],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['right', 'up']
                },

              'Red Room' : { 'down' : 'Hotel',
                  'left' : 'Alleyway',
                  'person'  : ['Yuffie'],
                  'resetHeartless' : ['Second District'],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['down', 'left']
                },

              'Alleyway' : { 'down' : 'Green Room',
                  'right' : 'Red Room',
                  'treasure' : '',
                  'heartless'  : '',
                  'resetHeartless' : ['Second District', 'Hotel'],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['right', 'down']
                },

              'Gizmo Shop' : { 'down' : 'Second District',
                    'up' : 'Second District Upper Side',
                    'heartless'  : '',
                    'resetHeartless' : ['Third District Upper Side', 'Hotel', 'Third District'],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['down', 'up']
             },

             'Second District Upper Side' : { 'down' : 'Gizmo Shop',
                    'right' : 'Third District Upper Side',
                    'jump' : 'Second District',
                    'heartless'  : '',
                    'resetHeartless' : ['Second District'],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['right', 'down', 'jump']
             },

             'Third District Upper Side' : { 'left' : 'Second District Upper Side',
                    'jump' : 'Third District',
                    'heartless'  : '',
                    'resetHeartless' : ['Gizmo Shop'],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['left', 'jump']
             },

             'Mystical House' : { 'down' : 'Third District',
                  'up' : 'Magician\'s Study',
                  'resetHeartless' : ['Second District'],
                  'map number' : '2',
                  'restricted' : {},
                  'move': ['down', 'up']
                },

              'Magician\'s Study' : { 'down' : 'Mystical House',
                  'elevator' : 'Cavern',
                  # 'person'  : ['Merlin', 'Fairy Godmother'],
                  'book': 'book',
                  'resetHeartless' : ['Third District', 'Alleyway'],
                  'Save':'',
                  'map number' : '2',
                  'restricted' : {},
                  'move': ['down', 'elevator']
                },

              '?' : { 'Merlin' : 'Magician\'s Study',
                  'person'  : ['Merlin'],
                  'map number' : '2',
                  'restricted' : {},
                  'move': []
                },

              'Cavern' : { 'down' : 'Alleyway',
                  'elevator' : 'Magician\'s Study',
                  'person'  : ['Kairi'],
                  'map number' : '2',
                  'restricted' : {},
                  'move': ['down']
                },

            'First District Shop' : { 'leave' : 'First District',              
                  'person'  : ['Moogle'],
                  'resetHeartless' : ['Second District', 'Hotel', 'Alleyway'],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['leave']
                },

            'Rooms List' : {
                  'resetHeartless' : ['First District', 'Second District', 'Third District', 'Small House',
                   'Dalmatian House', 'Hotel', 'Green Room', 'Red Room', 'Alleyway', 'Gizmo Shop', 'Second District Upper Side',
                   'Third District Upper Side', 'Mystical House', 'Magician\'s Study', '?', 'Cavern', 'First District Shop']
            }

  },


  'Wonderland':{

    0 : 'Rabbit Hole',

    'Rabbit Hole': {},

    'Bizarre Room': {},

    'Bizarre Room A': {},

    'Bizarre Room B': {},

    'Bizarre Room C': {},

    'Queen\'s Castle': {},

    'Lotus Forest': {},

    'Tea Party Garden': {},

    'Rooms List' : {
                  'resetHeartless' : ['Bizarre Room', 'Bizarre Room A',
                  'Bizarre Room B', 'Bizarre Room C', 'Lotus Forest', 'Tea Party Garden']
    }
  },



  'DeepJungle': {

      0:'',


      'Rooms List' : {
                  'resetHeartless' : []
    }

  },


    'Atlantica': {

      0:'',


      'Rooms List' : {
                  'resetHeartless' : []
    }

  },
  

  'OlympusColiseum': {

    0 : 'Coliseum Gates',

      'Coliseum Gates' : { 'up' : 'Lobby',
                  'person'  : ['Phil', 'Hercules'],
                  'resetHeartless' : [],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['up']
      }, 

      'Lobby' : { 'down' : 'Coliseum Gates',
                  # 'treasure' : '',
                  'person'  : ['Phil', 'Hercules'],
                  'shop' : 'Coliseum Shop',
                  'resetHeartless' : [],
                  'Save':'',
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['down']
      },

      'Coliseum Shop' : { 'leave' : 'Lobby',              
                  'person'  : ['Moogle'],
                  'resetHeartless' : [],
                  'map number' : '1',
                  'restricted' : {},
                  'key' : 'Coliseum Shop location',
                  'move': ['leave']
                },

      'Rooms List' : {
                  'resetHeartless' : ['Coliseum Gates', 'Lobby']
      }
  },


    'Agrabah': {

      0:'',


      'Rooms List' : {
                  'resetHeartless' : []
    }

  },


    'Monstro': {

      0:'',


      'Rooms List' : {
                  'resetHeartless' : []
    }

  },


    '100AcreWood': {

      0:'Old Book',

      'Old Book' : {
                  # 'one' : 'First Page',
                  # 'two' : 'Second Page',
                  # 'three' : 'Third Page',
                  # 'four' : 'Fourth Page',
                  # 'five' : 'Fifth Page',
                  'resetHeartless' : [],
                  'map number' : '0',
                  'restricted' : {},
                  'move': []
                  # 'move': ['one', 'two', 'three', 'four', 'five']
      },

      'Rooms List' : {
                  'resetHeartless' : ['Old Book', '', '', '', '', '']
    }

  },


    'HalloweenTown': {

      0:'',


      'Rooms List' : {
                  'resetHeartless' : []
    }

  },


    'Neverland': {

      0:'',


      'Rooms List' : {
                  'resetHeartless' : []
    }

  },


    'HollowBastion': {

      0:'',


      'Rooms List' : {
                  'resetHeartless' : []
    }

  },


    'EndOfTheWorld': {

      0:'',


      'Rooms List' : {
                  'resetHeartless' : []
    }

  },



  'CastleOblivion': {

    0 : '1st Floor',

      '1st Floor' : { 'right' : '2nd Floor',
                  'down' : '5th Floor',
                  'shop' : '1st Floor Shop',
                  'resetHeartless' : [],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['right', 'down']
      }, 

      '2nd Floor' : { 'right' : '3rd Floor',
                  'left' : '1st Floor',
                  'up' : '1st Floor',
                  'down' : '5th Floor',
                  'treasure' : '',
                  'person'  : ['Roxas', 'Axel'],
                  # 'heartless'  : '',
                  'resetHeartless' : [],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['right', 'down', 'left', 'up']
      },

      '3rd Floor' : { 'right' : '4th Floor',
                  'left' : '2nd Floor',
                  'up' : '1st Floor',
                  'down' : '5th Floor',
                  'resetHeartless' : [],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['right', 'down', 'left', 'up']
      },

      '4th Floor' : { 'right' : '5th Floor',
                  'left' : '3rd Floor',
                  'up' : '1st Floor',
                  'down' : '5th Floor',
                  'resetHeartless' : [],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['right', 'down', 'left', 'up']
      },

      '5th Floor' : {'left' : '4th Floor',
                  'up' : '1st Floor',
                  'boss' : 'Xemnas',
                  'heartless'  : '',
                  'resetHeartless' : [],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['left', 'up']
      },

      '1st Floor Shop' : { 'leave' : '1st Floor',              
                  'person'  : ['Moogle'],
                  'resetHeartless' : ['5th Floor'],
                  'map number' : '1',
                  'restricted' : {},
                  'move': ['leave']
                },

      
      'Rooms List' : {
                  'resetHeartless' : ['1st Floor', '2nd Floor', '3rd Floor', '4th Floor', '5th Floor', '1st Floor Shop']
      }

  }
}