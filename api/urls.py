import webapp2


routes = [
        webapp2.Route(r'/', handler='api.home.Home', name='home'),
        webapp2.Route(r'/love/<to_user:[A-Za-z_\d]+>/<from_user:[A-Za-z_\d]+>', handler='api.calls.Love', name='love'),
        webapp2.Route(r'/like/<to_user:[A-Za-z_\d]+>/<from_user:[A-Za-z_\d]+>', handler='api.calls.Like', name='like'),
        webapp2.Route(r'/miss/<to_user:[A-Za-z_\d]+>/<from_user:[A-Za-z_\d]+>', handler='api.calls.Miss', name='miss'),
        webapp2.Route(r'/snapchat/<to_user:[A-Za-z_\d]+>/<from_user:[A-Za-z_\d]+>', handler='api.calls.Snapchat', name='snapchat'),
        webapp2.Route(r'/everyone/<from_user:[A-Za-z_\d]+>', handler='api.calls.Everyone', name='everyone'),
        webapp2.Route(r'/thank/<what:[A-Za-z_\d]+>/<from_user:[A-Za-z_\d]+>', handler='api.calls.Thank', name='thank'),
]
