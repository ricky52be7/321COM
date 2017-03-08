import os

import webapp2
import jinja2

template_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), 'www/templates')
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('login.html')
        self.response.write(template.render())

    def post(self):
        self.response.write("nothing")


class MainHandler(webapp2.RedirectHandler):
    def get(self):
        self.response.write("123")


app = webapp2.WSGIApplication([
    ('/admin.*', MainHandler),
    ('/admin/login', LoginHandler),
], debug=True)
