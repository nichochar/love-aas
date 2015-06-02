import webapp2
from google.appengine.api.app_identity import get_default_version_hostname
from api.handlers import Handler404
from api.handlers import Handler500
from api.urls import routes as api_routes

MESSAGE_TEMPLATE_PATH = 'templates/message.html'

PRODUCTION_SERVER = 'iluaas.appspot.com'
is_production = get_default_version_hostname() == PRODUCTION_SERVER


app = webapp2.WSGIApplication(
    api_routes,
    debug=not is_production,
)

if is_production:
    app.error_handlers[404] = Handler404.get
    app.error_handlers[500] = Handler500.get
