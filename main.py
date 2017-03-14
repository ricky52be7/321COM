#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os

import webapp2
import jinja2

from entities.Brand import Brand
from entities.Category import Category
from entities.Order import Order
from entities.Account import Account
from google.appengine.api import users
from entities.Product import Product

template_dir = os.path.join(os.path.dirname(__file__), 'www/templates')
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            Account.get_or_create(user.user_id(), user.nickname())
            auth_link = users.create_logout_url(self.request.url)
        else:
            auth_link = users.create_login_url(self.request.url)

        template_var = {
            "auth_link": auth_link
        }
        template = JINJA_ENVIRONMENT.get_template('login.html')
        self.response.write(template.render())


class OrderAddHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('order_add.html')
        self.response.write(template.render())

    def post(self):
        user = users.get_current_user()
        name = self.request.get("name")
        desc = self.request.get("description", "")
        user = Account.get_or_create(user.user_id(), user.nickname())
        order = Order(name=name, description=desc, user=user)
        order.put()
        self.redirect("/order/add")


class OrderHandler(webapp2.RequestHandler):
    def get(self, order_id):
        order = Order.get_by_id(order_id)
        self.redirect("/")


class ProductAddHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('product_add.html')
        template_var = {
            "categories": Category.query().order(Category.name).fetch(),
            "brands": Brand.query().order(Brand.name).fetch(),
        }
        self.response.write(template.render(template_var))

    def post(self):
        name = self.request.get("name")
        desc = self.request.get("description")
        category = Category.get_by_id(self.request.get("category", 0))
        brand = Brand.get_by_id(self.request.get("brand", 0))
        product = Product(name=name, description=desc, category=category, brand=brand)
        product.put()
        self.redirect("/order/add")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/order/add', OrderAddHandler),  # change to /order/(\d+)/add, new Order before change page
    ('/order/(\d+)', OrderHandler),
    ('/order/product/add', ProductAddHandler)
], debug=True)
