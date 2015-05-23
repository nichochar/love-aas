import webapp2
from google.appengine.ext.webapp import template
from loveutils import messages
from loveutils import config


MESSAGE_TEMPLATE_PATH = 'templates/message.html'
HOME_TEMPLATE_PATH = 'templates/home.html'
MESSAGES = messages.MESSAGES


def handle_404():
    template_values = {
        'message': '404 not found. Oh NO! Nobody loves a 404!',
        'signature': 'The LoveMaster'
    }
    return template.render(MESSAGE_TEMPLATE_PATH, template_values)


class Home(webapp2.RequestHandler):
    def get(self):
        """
        Home index page handler
        """
        message_list = []
        for key, value in MESSAGES.iteritems():
            to_user_exists = True if 'to_user' in value else False
            message_list.append({
                'key': key,
                'to_user_exists': to_user_exists,
                'formatted_message': value.format(to_user=':to_user')
            })

        template_values = {
            'message_list': message_list,
            'app_version': config.APP_VERSION
        }
        return self.response.out.write(
            template.render(HOME_TEMPLATE_PATH, template_values)
        )


class Message(webapp2.RequestHandler):
    def get(self, key, user1=None, user2=None):
        """
        Spreads the love from from_user to to user
        Message handler
        """
        # Make sure we have the right to/from depending on number of args
        if user2:
            to_user = user1
            from_user = user2
        else:
            to_user = None
            from_user = user1

        # Make sure we support this love message
        acceptable_keys = [r for r in MESSAGES]
        if key not in acceptable_keys:
            return self.response.out.write(handle_404())

        # Map and format the message and signature
        message = MESSAGES[key].format(to_user=to_user)
        signature = from_user
        template_values = {
            'message': message,
            'signature': signature,
        }

        view = template.render(MESSAGE_TEMPLATE_PATH, template_values)
        return self.response.out.write(view)
