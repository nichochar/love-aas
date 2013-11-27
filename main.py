import webapp2
import logging
from webapp2_extras import routes
from google.appengine.ext.webapp import template

from api.urls import routes as api_routes

class BaseHandler(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render_template(self, filename, **template_args):
        self.response.write(self.jinja2.render_template(filename, **template_args))

def handle_404(request, response, exception):
    template_values = {
            'message':'404 not found. Oh NO! Nobody loves a 404!',
            'signature':'The LoveMaster'
            }
    response.out.write(template.render('templates/main_template.html', template_values))

def handle_500(request, response, exception):
    template_values = {
            'message':'500 server error. Oh NO! Nobody loves a 500!',
            'signature':'The LoveMaster'
            }
    response.out.write(template.render('templates/main_template.html', template_values))

app = webapp2.WSGIApplication(
        api_routes,
        debug=True,
)
app.error_handlers[404] = handle_404
app.error_handlers[500] = handle_500
