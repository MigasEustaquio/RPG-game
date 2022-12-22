# TUTORIAL
# world:{
#     room:{
#         story:{
#             'waves': (number of waves), 'status': (current wave),
#             'wave': {(wave number): (enemy in the wave)}
#         }
#     }
# }

enemyLocations = {

    'DestinyIslands': {

        'Dive to the Heart 3':{
            0:{
                'waves': 1, 'status': 1,
                'wave': {1: 'shadow'}
            }
        }
    },

    'TraverseTown': {

        'Second District':{
            0:{
                'waves' : 2, 'status' : 2,
                'wave' : {2 : 'soldier', 1 : 'shadow'}
            },
            1:{
                'waves' : 2, 'status' : 2,
                'wave' : {2 : 'soldier', 1 : 'shadow'}
            },
        },

        'Hotel': {
            0:{
                'waves' : 1, 'status' : 1,
                'wave' : {1 : 'shadow'}
            },
            1:{
                'waves' : 1, 'status' : 1,
                'wave' : {1 : 'shadow'}
            },
        },

        'Alleyway': {
            0:{
                'waves' : 3, 'status' : 3,
                'wave' : {3 : 'soldier', 2 : 'shadow', 1 : 'shadow'}
            },
            1:{
                'waves' : 3, 'status' : 3,
                'wave' : {3 : 'soldier', 2 : 'shadow', 1 : 'shadow'}
            },
        },

        'Gizmo Shop':{
            0:{
                'waves' : 1, 'status' : 1,
                'wave' : {1 : 'shadow'}
            },
            1:{
                'waves' : 1, 'status' : 1,
                'wave' : {1 : 'shadow'}
            },
        },

        'Second District Upper Side':{
            0:{
                'waves' : 1, 'status' : 1,
                'wave' : {1 : 'shadow'}
            },
            1:{
                'waves' : 1, 'status' : 1,
                'wave' : {1 : 'shadow'}
            },
        },

        'Third District Upper Side':{
            0:{
                'waves' : 1, 'status' : 1,
                'wave' : {1 : 'shadow'}
            },
            1:{
                'waves' : 1, 'status' : 1,
                'wave' : {1 : 'shadow'}
            },
        },


    },

    'CastleOblivion':{

        '5th Floor':{
            2: {
                'waves' : 1, 'status' : 1,
                'wave' : { 1 : 'soldier'}
            },
            3: {
                'waves' : 1, 'status' : 1,
                'wave' : { 1 : 'invisible'}
            },
        }
    }

}