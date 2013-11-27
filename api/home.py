import webapp2
from google.appengine.ext.webapp import template


class Home(webapp2.RequestHandler):
    def get(self):
        """
        Home page with API explanations
        """

        self.response.out.write(template.render('templates/home.html', None))
