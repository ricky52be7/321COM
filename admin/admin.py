import os

import webapp2
import jinja2

from google.appengine.api import users

template_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), 'www/templates')
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RedirectHandler):
    def get(self):
        user = users.get_current_user()
        # self.response.write(user.auth_domain())
        template = JINJA_ENVIRONMENT.get_template('dashboard.html')
        template_var = {
            "logout": users.create_logout_url(self.request.path)
        }
        self.response.write(template.render(template_var))


app = webapp2.WSGIApplication([
    ('/admin.*', MainHandler),
], debug=True)
