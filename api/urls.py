import webapp2

routes = [
    webapp2.Route(
        r'/',
        handler='api.handlers.Home',
        name='home'
    ),
    webapp2.Route(
        r'/404',
        handler='api.handlers.Handler404',
        name='404'
    ),
    webapp2.Route(
        r'/500',
        handler='api.handlers.Handler500',
        name='500'
    ),
    webapp2.Route(
        r'/create/<key:(\w+)>',
        handler='api.handlers.Create',
        name='create1'
    ),
    webapp2.Route(
        r'/create',
        handler='api.handlers.CreateGuided',
        name='create-guided'
    ),
    webapp2.Route(
        r'/create/',
        handler='api.handlers.CreateGuided',
        name='create-guided-slash'
    ),
    webapp2.Route(
        r'/<key:([A-Za-z]+ ?)+?>/<user1:([A-Za-z_\d]+ ?)+?>/<user2:([A-Za-z_\d]+ ?)+?>',
        handler='api.handlers.Message',
        name='message2params'
    ),
    webapp2.Route(
        r'/<key:([A-Za-z]+ ?)+?>/<user1:([A-Za-z_\d]+ ?)+?>/<user2:([A-Za-z_\d]+ ?)+?>/',
        handler='api.handlers.Message',
    ),
    webapp2.Route(
        r'/<key:([A-Za-z]+ ?)+?>/<user1:([A-Za-z_\d]+ ?)+?>',
        handler='api.handlers.Message',
        name='message1param'
    ),
    webapp2.Route(
        r'/<key:([A-Za-z]+ ?)+?>/<user1:([A-Za-z_\d]+ ?)+?>/',
        handler='api.handlers.Message',
    ),
]
