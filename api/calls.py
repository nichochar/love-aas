import json
import webapp2
import os
from webapp2_extras import jinja2
from google.appengine.ext.webapp import template

class Love(webapp2.RequestHandler):
    def get(self, to_user, from_user):
        """
        Spreads the love from from_user to to_user
        """

        message = "Hi {to_user}, I love you".format(to_user=to_user)
        signature = from_user
        template_values = {
                'message':message,
                'signature':signature,
                }

        #path = os.path.join(os.path.dirname(__file__), 'main_template.html')

        self.response.out.write(template.render('templates/main_template.html', template_values))
