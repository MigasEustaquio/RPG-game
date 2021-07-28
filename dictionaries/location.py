#a dictionary linking a room to other room positions
rooms = {
  'TraverseTown' : {

    0 : 'First District',

            'First District' : { 'up' : 'Second District',
                  'shop' : 'First District Shop',
                  'resetHeartless' : ['Hotel', 'Alleyway']
            },        

            'Second District' : { 'down' : 'First District',
                  'right' : 'Third District',
                  'left' : 'Hotel',
                  'treasure' : {'treasure' : 'item', 'item' : 'potion'},
                  'heartless'  : { 
                    'waves' : 2, 'status' : 2, 'wave' : {
                       2 : 'soldier', 1 : 'shadow'}
                  },
                  'resetHeartless' : ['Alleyway']
                },
                
            'Third District' : { 'left'  : 'Second District',
                                'resetHeartless' : ['Hotel', 'Alleyway']
                },
                
            'Hotel' : { 'right' : 'Second District',
                    'left' : 'Green Room',
                    'up' : 'Red Room',
                    'heartless'  : { 
                    'waves' : 1, 'status' : 1, 'wave' : {
                        1 : 'shadow'}
                    },
                    'resetHeartless' : ['Alleyway']
             },

             'Green Room' : { 'right' : 'Hotel',
                  'up' : 'Alleyway',
                  'person'  : 'Leon',
                  'resetHeartless' : ['Second District']
                },

              'Red Room' : { 'down' : 'Hotel',
                  'left' : 'Alleyway',
                  'person'  : 'Yuffie',
                  'resetHeartless' : ['Second District']
                },

              'Alleyway' : { 'down' : 'Green Room',
                  'right' : 'Red Room',
                  'treasure' : {'treasure' : 'mapUpdate', 'mapUpdate' : 'heartless '},
                  'heartless'  : { 
                    'waves' : 3, 'status' : 3, 'wave' : {
                       3 : 'soldier', 2 : 'shadow', 1 : 'shadow'}
                  },
                  'resetHeartless' : ['Second District', 'Hotel']
                },

            'First District Shop' : { 'person'  : 'Moogle',
                                    'resetHeartless' : ['Second District', 'Hotel', 'Alleyway']
                },

  },


  'CastleOblivion': {

    0 : '1st Floor',

      '1st Floor' : { 'right' : '2nd Floor',
                  'down' : '5th Floor',
                  'shop' : '1st Floor Shop',
                  'resetHeartless' : []
      }, 

      '2nd Floor' : { 'right' : '3rd Floor',
                  'left' : '1st Floor',
                  'up' : '1st Floor',
                  'down' : '5th Floor',
                  'heartless'  : { 
                    'waves' : 1, 'status' : 1, 'wave' : { 1 : 'angel star'}
                  },
                  'resetHeartless' : []
      },

      '3rd Floor' : { 'right' : '4th Floor',
                  'left' : '2nd Floor',
                  'up' : '1st Floor',
                  'down' : '5th Floor',
                  'resetHeartless' : []
      },

      '4th Floor' : { 'right' : '5th Floor',
                  'left' : '3rd Floor',
                  'up' : '1st Floor',
                  'down' : '5th Floor',
                  'resetHeartless' : []
      },

      '5th Floor' : {'left' : '4th Floor',
                  'up' : '1st Floor',
                  'heartless'  : { 
                    'waves' : 1, 'status' : 1, 'wave' : { 1 : 'invisible'}
                  },
                  'resetHeartless' : []
      },

      '1st Floor Shop' : { 'person'  : 'Moogle',
                  'resetHeartless' : []
                },

  }



         }