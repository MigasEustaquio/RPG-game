#a dictionary linking a room to other room positions
rooms = {

            'First District' : { 'up' : 'Second District',
                  'shop' : 'First District Shop'
            },        

            'Second District' : { 'down' : 'First District',
                  'right' : 'Third District',
                  'left' : 'Hotel',
                  'heartless'  : 'shadow'
                },
                
            'Third District' : { 'left'  : 'Second District',              
                },
                
            'Hotel' : { 'right' : 'Second District',
                    'left' : 'Green Room',
                    'up' : 'Red Room',
                    'heartless'  : 'shadow'
                    
             },

             'Green Room' : { 'right' : 'Hotel',
                  'up' : 'Alleyway',
                  'person'  : 'Leon'
                },

              'Red Room' : { 'down' : 'Hotel',
                  'left' : 'Alleyway',
                  'person'  : 'Yuffie'
                },

              'Alleyway' : { 'down' : 'Green Room',
                  'right' : 'Red Room',
                  'heartless'  : 'soldier'
                },

            'First District Shop' : { 'person'  : 'Moogle',              
                },

         }