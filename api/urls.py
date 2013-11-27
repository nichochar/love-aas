import webapp2


routes = [
        webapp2.Route(r'/love/<to_user:[A-Za-z_]+>/<from_user:[A-Za-z_]+>', handler='api.calls.Love', name='love'),
]
