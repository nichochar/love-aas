import webapp2


routes = [
        webapp2.Route(r'/', handler='api.home.Home', name='home'),
        webapp2.Route(r'/love/<to_user:([A-Za-z_\d]+ ?)+?>/<from_user:([A-Za-z_\d]+ ?)+?>', handler='api.calls.Love', name='love'),
        webapp2.Route(r'/like/<to_user:([A-Za-z_\d]+ ?)+?>/<from_user:([A-Za-z_\d]+ ?)+?>', handler='api.calls.Like', name='like'),
        webapp2.Route(r'/miss/<to_user:([A-Za-z_\d]+ ?)+?>/<from_user:([A-Za-z_\d]+ ?)+?>', handler='api.calls.Miss', name='miss'),
        webapp2.Route(r'/snapchat/<to_user:([A-Za-z_\d]+ ?)+?>/<from_user:([A-Za-z_\d]+ ?)+?>', handler='api.calls.Snapchat', name='snapchat'),
        webapp2.Route(r'/everyone/<from_user:([A-Za-z_\d]+ ?)+?>', handler='api.calls.Everyone', name='everyone'),
        webapp2.Route(r'/thank/<what:([A-Za-z_\d]+ ?)+?>/<from_user:([A-Za-z_\d]+ ?)+?>', handler='api.calls.Thank', name='thank'),
        webapp2.Route(r'/request/<to_user:([A-Za-z_\d]+ ?)+?>/<from_user:([A-Za-z_\d]+ ?)+?>', handler='api.calls.Request', name='request'),
        webapp2.Route(r'/reply/<to_user:([A-Za-z_\d]+ ?)+?>/<from_user:([A-Za-z_\d]+ ?)+?>', handler='api.calls.Reply', name='reply'),
        webapp2.Route(r'/kiss/<to_user:([A-Za-z_\d]+ ?)+?>/<from_user:([A-Za-z_\d]+ ?)+?>', handler='api.calls.Kiss', name='kiss'),
        webapp2.Route(r'/cuddle/<to_user:([A-Za-z_\d]+ ?)+?>/<from_user:([A-Za-z_\d]+ ?)+?>', handler='api.calls.Cuddle', name='cuddle'),
        webapp2.Route(r'/crush/<to_user:([A-Za-z_\d]+ ?)+?>/<from_user:([A-Za-z_\d]+ ?)+?>', handler='api.calls.Crush', name='crush'),
        webapp2.Route(r'/thanksgiving/<to_user:([A-Za-z_\d]+ ?)+?>/<from_user:([A-Za-z_\d]+ ?)+?>', handler='api.calls.Thanksgiving', name='thanksgiving'),
        webapp2.Route(r'/owe/<to_user:([A-Za-z_\d]+ ?)+?>/<from_user:([A-Za-z_\d]+ ?)+?>', handler='api.calls.Owe', name='owe'),
]
