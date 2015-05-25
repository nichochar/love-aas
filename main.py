import webapp2
import logging
from google.appengine.ext.webapp import template
from google.appengine.api.app_identity import get_default_version_hostname

from api.urls import routes as api_routes
MESSAGE_TEMPLATE_PATH = 'templates/message.html'

PRODUCTION_SERVER = 'iluaas.appspot.com'
is_production = get_default_version_hostname() == PRODUCTION_SERVER


def handle_404(request, response, exception):
    template_values = {
        'message': '404 not found. Oh NO! Nobody loves a 404!',
        'signature': 'The LoveMaster'
    }
    logging.error(exception)
    return response.out.write(
        template.render(MESSAGE_TEMPLATE_PATH, template_values)
    )


def handle_500(request, response, exception):
    template_values = {
        'message': '500 server error. Oh NO! Nobody loves a 500!',
        'signature': 'The LoveMaster'
    }
    logging.error(exception)
    return response.out.write(
        template.render(MESSAGE_TEMPLATE_PATH, template_values)
    )

app = webapp2.WSGIApplication(
    api_routes,
    debug=True,
)

if is_production:
    app.error_handlers[404] = handle_404
    app.error_handlers[500] = handle_500
