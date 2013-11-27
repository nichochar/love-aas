import webapp2
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

        self.response.out.write(template.render('templates/main_template.html', template_values))

class Like(webapp2.RequestHandler):
    def get(self, to_user, from_user):
        """
        Spreads the friendship from from_user to to_user
        """

        message = "Hi {to_user}, I like you, like a lot.".format(to_user=to_user)
        signature = from_user
        template_values = {
                'message':message,
                'signature':signature,
                }

        self.response.out.write(template.render('templates/main_template.html', template_values))

class Miss(webapp2.RequestHandler):
    def get(self, to_user, from_user):
        """
        Spreads the missing feeling from from_user to to_user
        """

        message = "Hi {to_user}, I miss you, so much.".format(to_user=to_user)
        signature = from_user
        template_values = {
                'message':message,
                'signature':signature,
                }

        self.response.out.write(template.render('templates/main_template.html', template_values))

class Snapchat(webapp2.RequestHandler):
    def get(self, to_user, from_user):
        """
        Spreads the snapchat urge 
        """

        message = "Hi {to_user}, in the name of love, snapchat me!".format(to_user=to_user)
        signature = from_user
        template_values = {
                'message':message,
                'signature':signature,
                }

        self.response.out.write(template.render('templates/main_template.html', template_values))

class Everyone(webapp2.RequestHandler):
    def get(self, from_user):
        """
        Spreads the snapchat urge 
        """

        message = "I love everyone!"
        signature = from_user
        template_values = {
                'message':message,
                'signature':signature,
                }

        self.response.out.write(template.render('templates/main_template.html', template_values))

class Thank(webapp2.RequestHandler):
    def get(self, what,from_user):
        """
        Spreads the snapchat urge 
        """

        message = "Thank you for {what}.".format(what=what)
        signature = from_user
        template_values = {
                'message':message,
                'signature':signature,
                }

        self.response.out.write(template.render('templates/main_template.html', template_values))
