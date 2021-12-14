#a dictionary linking a room to other room positions

# 'heartless' : (story)

roomsbk = {
  'TraverseTown' : {

    0 : 'First District',

            'First District' : { 'up' : 'Second District',
                  'shop' : 'First District Shop',
                  'resetHeartless' : ['Hotel', 'Alleyway'],
                  'map number' : '1'
            },        

            'Second District' : { 'down' : 'First District',
                  'right' : 'Third District',
                  'left' : 'Hotel',
                  'treasure' : {'treasure' : 'item', 'item' : 'potion'},
                  'heartless'  : { 
                    0:{
                    'waves' : 2, 'status' : 2, 'wave' : {
                       2 : 'soldier', 1 : 'shadow'}
                    },
                    1:{
                    'waves' : 2, 'status' : 2, 'wave' : {
                       2 : 'soldier', 1 : 'shadow'}
                    },
                  },
                  'resetHeartless' : ['Alleyway'],
                  'map number' : '1'
                },
                
            'Third District' : { 'left'  : 'Second District',
                                'resetHeartless' : ['Hotel', 'Alleyway'],
                  'map number' : '1'
                },
                
            'Hotel' : { 'right' : 'Second District',
                    'left' : 'Green Room',
                    'up' : 'Red Room',
                    'heartless'  : { 
                      0:{
                      'waves' : 1, 'status' : 1, 'wave' : {
                          1 : 'shadow'}
                      },
                      1:{
                      'waves' : 1, 'status' : 1, 'wave' : {
                          1 : 'shadow'}
                      },
                    },
                    'resetHeartless' : ['Alleyway'],
                  'map number' : '1'
             },

             'Green Room' : { 'right' : 'Hotel',
                  'up' : 'Alleyway',
                  'person'  : ['Leon'],
                  'resetHeartless' : ['Second District'],
                  'map number' : '1'
                },

              'Red Room' : { 'down' : 'Hotel',
                  'left' : 'Alleyway',
                  'person'  : ['Yuffie'],
                  'resetHeartless' : ['Second District'],
                  'map number' : '1'
                },

              'Alleyway' : { 'down' : 'Green Room',
                  'right' : 'Red Room',
                  'treasure' : {'treasure' : 'mapUpdate', 'mapUpdate' : '1'},
                  'heartless'  : { 
                    0:{
                      'waves' : 3, 'status' : 3, 'wave' : {
                        3 : 'soldier', 2 : 'shadow', 1 : 'shadow'}
                    },
                    1:{
                      'waves' : 3, 'status' : 3, 'wave' : {
                        3 : 'soldier', 2 : 'shadow', 1 : 'shadow'}
                    },
                  },
                  'resetHeartless' : ['Second District', 'Hotel'],
                  'map number' : '1'
                },

            'First District Shop' : { 'person'  : ['Moogle'],
                                    'resetHeartless' : ['Second District', 'Hotel', 'Alleyway'],
                  'map number' : '1'
                },

  },


  'CastleOblivion': {

    0 : '1st Floor',

      '1st Floor' : { 'right' : '2nd Floor',
                  'down' : '5th Floor',
                  'shop' : '1st Floor Shop',
                  'resetHeartless' : [],
                  'map number' : '1'
      }, 

      '2nd Floor' : { 'right' : '3rd Floor',
                  'left' : '1st Floor',
                  'up' : '1st Floor',
                  'down' : '5th Floor',
                  'treasure' : {'treasure' : 'keyblade', 'keyblade' : 'Kingdom Key D'},
                  'person'  : ['Roxas', 'Axel'],
                  # 'heartless'  : { 
                  #   1 : {
                  #   'waves' : 2, 'status' : 2, 'wave' : {
                  #      2 : 'soldier', 1 : 'shadow'}
                  #   },
                  #   3 : {
                  #   'waves' : 1, 'status' : 1, 'wave' : { 1 : 'angel star'}
                  #   },
                  # },
                  'resetHeartless' : [],
                  'map number' : '1'
      },

      '3rd Floor' : { 'right' : '4th Floor',
                  'left' : '2nd Floor',
                  'up' : '1st Floor',
                  'down' : '5th Floor',
                  'resetHeartless' : [],
                  'map number' : '1'
      },

      '4th Floor' : { 'right' : '5th Floor',
                  'left' : '3rd Floor',
                  'up' : '1st Floor',
                  'down' : '5th Floor',
                  'resetHeartless' : [],
                  'map number' : '1'
      },

      '5th Floor' : {'left' : '4th Floor',
                  'up' : '1st Floor',
                  'boss' : 'Xemnas',
                  'heartless'  : { 
                    2: {
                      'waves' : 1, 'status' : 1, 'wave' : { 1 : 'invisible'}
                    },
                    3: {
                      'waves' : 1, 'status' : 1, 'wave' : { 1 : 'invisible'}
                    },
                  },
                  'resetHeartless' : [],
                  'map number' : '1'
      },

      '1st Floor Shop' : { 'person'  : ['Moogle'],
                  'resetHeartless' : [],
                  'map number' : '1'
                },

  }



         }