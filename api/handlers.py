import webapp2
from google.appengine.ext.webapp import template
from loveutils import messages
from loveutils import config


MESSAGE_TEMPLATE_PATH = 'templates/message.html'
HOME_TEMPLATE_PATH = 'templates/home.html'
CREATE_TEMPLATE_PATH = 'templates/create.html'
MESSAGES = messages.MESSAGES


def handle_404():
    template_values = {
        'message': '404 not found. Oh NO! Nobody loves a 404!',
        'signature': 'The LoveMaster'
    }
    return template.render(MESSAGE_TEMPLATE_PATH, template_values)


def format_messages_for_views():
    '''
    Takes the MESSAGES from messages.MESSAGES and formats it
    from a dict with <key> : <value> to a list of the form:
    [(True, <key>, <message with "Recipient" formatted in),...]
    The first boolean signals if there is indeed a Recipient or not
    '''
    message_list = []
    for key, value in MESSAGES.iteritems():
        recipient_exists = True if 'to_user' in value else False
        message_list.append({
            'key': key,
            'to_user_exists': recipient_exists,
            'formatted_message': value.format(to_user='Recipient')
        })

    return message_list


class Home(webapp2.RequestHandler):
    def get(self):
        """
        Home index page handler
        """
        message_list = format_messages_for_views()
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
            'key': key,
            'recipient': to_user,
        }

        view = template.render(MESSAGE_TEMPLATE_PATH, template_values)
        return self.response.out.write(view)


class Create(webapp2.RequestHandler):
    def get(self, key):
        '''
        This page allows you to select a message to create
        '''
        # Make sure we support this love message
        acceptable_keys = [r for r in MESSAGES]
        if key not in acceptable_keys:
            return self.response.out.write(handle_404())

        message = MESSAGES[key]
        splitter = "%&*#"
        formatted_message = message.format(to_user=splitter)
        if splitter in formatted_message:
            part1, part2 = formatted_message.split(splitter)
            template_values = {
                'message_part1': part1,
                'message_part2': part2,
            }
        else:
            template_values = {
                'message_part1': formatted_message,
                'message_part2': None
            }
        view = template.render(CREATE_TEMPLATE_PATH, template_values)
        return self.response.out.write(view)
