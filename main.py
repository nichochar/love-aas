import webapp2
import logging
from webapp2_extras import routes

from api.urls import routes as api_routes

class BaseHandler(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render_template(self, filename, **template_args):
        self.response.write(self.jinja2.render_template(filename, **template_args))

app = webapp2.WSGIApplication(
        api_routes,
        debug=True,
)
