#a dictionary linking a room to other room positions
rooms = {

            'First District' : { 'north' : 'Second District',
                  'shop' : 'First District Shop'
            },        

            'Second District' : { 'south' : 'First District',
                  'east' : 'Third District',
                  'west' : 'Hotel',
                  'heartless'  : 'shadow'
                },
                
            'Third District' : { 'west'  : 'Second District',              
                },
                
            'Hotel' : { 'east' : 'Second District',
                    'west' : 'Green Room',
                    'north' : 'Red Room',
                    'heartless'  : 'shadow'
                    
             },

             'Green Room' : { 'east' : 'Hotel',
                  'north' : 'Alleyway',
                  'person'  : 'Leon'
                },

              'Red Room' : { 'south' : 'Hotel',
                  'west' : 'Alleyway',
                  'person'  : 'Yuffie'
                },

              'Alleyway' : { 'south' : 'Green Room',
                  'east' : 'Red Room',
                  'heartless'  : 'soldier'
                },

            'First District Shop' : { 'person'  : 'Moogle',              
                },

         }