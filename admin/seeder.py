from random import choice
from string import lowercase

import webapp2

from entities.Brand import Brand
from entities.Category import Category


def get_random_string(n):
    return "".join(choice(lowercase) for i in range(n))


class CategorySeederHandler(webapp2.RequestHandler):
    def get(self):
        Category.get_or_create("")
        Category.get_or_create("Test")
        self.response.write("finish")


class BrandSeederHandler(webapp2.RequestHandler):
    def get(self):
        Brand.get_or_create("")
        self.response.write("finish")

app = webapp2.WSGIApplication([
    ('/seeding/category', CategorySeederHandler),
    ('/seeding/brand', BrandSeederHandler),
], debug=True)
