import webapp2

routes = [
    webapp2.Route(
        r'/',
        handler='api.handlers.Home',
        name='home'
    ),
    webapp2.Route(
        r'/<key:([A-Za-z]+ ?)+?>/<user1:([A-Za-z_\d]+ ?)+?>/<user2:([A-Za-z_\d]+ ?)+?>',
        handler='api.handlers.Message',
        name='message'
    ),
    webapp2.Route(
        r'/<key:([A-Za-z]+ ?)+?>/<user1:([A-Za-z_\d]+ ?)+?>/<user2:([A-Za-z_\d]+ ?)+?>/',
        handler='api.handlers.Message',
        name='message'
    ),
    webapp2.Route(
        r'/<key:([A-Za-z]+ ?)+?>/<user1:([A-Za-z_\d]+ ?)+?>',
        handler='api.handlers.Message',
        name='message'
    ),
    webapp2.Route(
        r'/<key:([A-Za-z]+ ?)+?>/<user1:([A-Za-z_\d]+ ?)+?>/', 
        handler='api.handlers.Message', 
        name='message'
    ),
]
