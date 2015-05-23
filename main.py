import webapp2
import logging
from google.appengine.ext.webapp import template

from api.urls import routes as api_routes
MESSAGE_TEMPLATE_PATH = 'templates/message.html'


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
app.error_handlers[404] = handle_404
app.error_handlers[500] = handle_500
