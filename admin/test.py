import webapp2
from google.appengine.api import mail, users

from entities.Order import Order


class TestHandler(webapp2.RequestHandler):
    def get(self):
        """
        name = self.request.get("name", "")
        category = self.request.get("category", "")
        brand = self.request.get("brand", "")
        self.response.write(Order.search(name, category, brand)) 
        """
        mail.send_mail(sender="321com@com-159616.appspotmail.com",
                       to=users.User(_user_id=users.get_current_user().user_id()).email(),
                       subject="test",
                       body="test")
        self.response.write("finish")


app = webapp2.WSGIApplication([
    ('/test', TestHandler),
], debug=True)
