import webapp2

from entities.Order import Order


class TestHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get("name", "")
        category = self.request.get("category", "")
        brand = self.request.get("brand", "")
        self.response.write(Order.search(name, category, brand))


app = webapp2.WSGIApplication([
    ('/test', TestHandler),
], debug=True)
