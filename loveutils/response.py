import json
import webapp2
from google.appengine.ext.webapp import template


class LoveResponse(webapp2.Response):
    def __init__(self, message, signature, accepts=None, *args, **kwargs):
        super (LoveResponse, self).__init__(*args, **kwargs)
        self.accepts = accepts

        # Set it to HTML if not request type asked for
        if not self.accepts:
            self.accepts = 'text/plain'

        if self.accepts.lower() not in ('application/json', 'text/plain'):
            self.status_int = 403

            # Skip the rest of the method
            return

        message += ' -- {from_user}'.format(from_user=signature)
        if self.accepts == 'application/json':

            body = json.dumps(
                {
                    'status': self.status_int,
                    'message': message,
                }
            )

        elif self.accepts == 'text/plain':
            body = message
