import webapp2

from entities.Account import Account
from entities.Brand import Brand
from entities.Category import Category
from entities.Order import Order
from google.appengine.api import users


class CategorySeederHandler(webapp2.RequestHandler):
    def get(self):
        Category.seed()
        self.response.write("finish")


class BrandSeederHandler(webapp2.RequestHandler):
    def get(self):
        Brand.seed()
        self.response.write("finish")


class SeederHandler(webapp2.RequestHandler):
    def get(self):
        Category.seed()
        Brand.seed()
        # user = users.get_current_user()
        # account = Account(id=user.user_id(), name=user.nickname())
        # Order.seed(account)
        self.response.write("finish")


class OrderSeederHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        account = Account(id=user.user_id(), name=user.nickname())
        Order.seed(account)
        self.response.write("finish")


app = webapp2.WSGIApplication([
    ('/seeding/category', CategorySeederHandler),
    ('/seeding/brand', BrandSeederHandler),
    ('/seeding/order', OrderSeederHandler),
    ('/seeding/all', SeederHandler),
], debug=True)
