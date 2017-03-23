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
import logging

from entities.Brand import Brand
from entities.Category import Category
from entities.Offer import Offer
from entities.Order import Order
from entities.Account import Account
from entities.Trade import Trade
from google.appengine.api import users
from google.appengine.api import images
from google.appengine.ext import ndb

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


class OrderRedirectHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        order = Order(name="",
                      description="",
                      products=[],
                      user=Account.get_or_create(user.user_id(), user.nickname()))
        order.put()
        self.redirect("/order/"+str(order.key.id()))


class OrderAddHandler(webapp2.RequestHandler):
    def get(self, order_id):
        order = Order.get_by_id(int(order_id))
        template = JINJA_ENVIRONMENT.get_template('order_add.html')
        template_var = {
            "isAdmin": users.is_current_user_admin(),
            "order": order,
            "products": order.products,
            "status": Order.STATUS
        }
        self.response.write(template.render(template_var))

    def post(self, order_id):
        user = users.get_current_user()
        name = str(self.request.get("name", ""))
        desc = str(self.request.get("description", ""))
        account = Account.get_or_create(user.user_id(), user.nickname())
        order = Order.get_by_id(int(order_id))
        status = int(self.request.get("status", order.status))
        order.name = name
        order.description = desc
        order.user = account
        order.status = status
        order.put()
        if users.is_current_user_admin():
            self.redirect("/admin")
        else:
            self.redirect("/" + str(user.user_id()) + "/orders")


class ProductAddHandler(webapp2.RequestHandler):
    def get(self, order_id):
        template = JINJA_ENVIRONMENT.get_template('product_add.html')
        template_var = {
            "categories": Category.query().order(Category.name).fetch(),
            "brands": Brand.query().order(Brand.name).fetch(),
            # "img": Product.query().order(Product.img).fetch()
            # self.response.out.write('<div><img src="/img?img_id=%s"></img>' %
            #                         greeting.key.urlsafe())
            # self.response.out.write('<blockquote>%s</blockquote></div>' %
            #                         cgi.escape(greeting.content))
        }
        self.response.write(template.render(template_var))

    def post(self, order_id):
        name = self.request.get("name")
        desc = self.request.get("description")
        category = Category.get_by_id(int(self.request.get("category")))
        # status = self.request.get("status")
        brand = Brand.get_by_id(int(self.request.get("brand")))
        # img = self.request.get("photo", None)
        product = Product(name=name, description=desc, category=category, brand=brand)
        # product = Product(name=name, description=desc, category=category, brand=brand, img=img)
        # product.put()
        order = Order.get_by_id(int(order_id))
        order.products.append(product)
        order.put()
        self.redirect("/order/" + str(order.key.id()))


class HomepageHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            Account.get_or_create(user.user_id(), user.nickname())
            auth_link = users.create_logout_url(self.request.url)
        else:
            auth_link = users.create_login_url(self.request.url)
        template = JINJA_ENVIRONMENT.get_template('homepage.html')
        template_var = {
            "categories": Category.query().order(Category.name).fetch(),
            "brands": Brand.query().order(Brand.name).fetch(),
            "orders": Order.query(Order.status == Order.STATUS_VALID).order(Order.create_at).fetch(),
            "users": users,
            "auth_link": auth_link,
        }
        self.response.write(template.render(template_var))


class Image(webapp2.RequestHandler):
    def get(self):
        greeting_key = ndb.Key(urlsafe=self.request.get('img_id'))
        greeting = greeting_key.get()
        if greeting.avatar:
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(greeting.avatar)
        else:
            self.response.out.write('No image')


class MyOrdersHandler(webapp2.RequestHandler):
    def get(self, user_id):
        template = JINJA_ENVIRONMENT.get_template('my_order.html')
        template_var = {
            "categories": Category.query().order(Category.name).fetch(),
            "brands": Brand.query().order(Brand.name).fetch(),
            "orders": Order.get_my_order(),
            "users": users,
        }
        self.response.write(template.render(template_var))


class OrderViewHandler(webapp2.RequestHandler):
    def get(self, order_id):
        template = JINJA_ENVIRONMENT.get_template('order_view.html')
        order = Order.get_by_id(int(order_id))
        template_var = {
            "categories": Category.query().order(Category.name).fetch(),
            "products": order.products,
            "order": order,
            "users": users,
            "offers": Trade.get_trade_offer(order.key.id())
        }
        self.response.write(template.render(template_var))


class OfferRedirectHandler(webapp2.RequestHandler):
    def get(self, order_id):
        user = users.get_current_user()
        offer = Offer(name="",
                      description="",
                      products=[],
                      user=Account.get_or_create(user.user_id(), user.nickname()))
        offer.put()
        self.redirect("/order/"+order_id+"/offer/"+str(offer.key.id()))


class OfferAddHandler(webapp2.RequestHandler):
    def get(self, order_id, offer_id):
        template = JINJA_ENVIRONMENT.get_template('offer_add.html')
        offer = Offer.get_by_id(int(offer_id))
        template_var = {
            "products": offer.products,
            "offer": offer,
            "order_id": order_id,
        }
        self.response.write(template.render(template_var))

    def post(self, order_id, offer_id):
        trade = Trade(order=int(order_id), offer=int(offer_id))
        trade.put()
        self.redirect("/order/"+order_id+"/view")


class AddOfferProductHandler(webapp2.RequestHandler):
    def get(self, order_id, offer_id):
        template = JINJA_ENVIRONMENT.get_template('product_add.html')
        template_var = {
            "categories": Category.query().order(Category.name).fetch(),
            "brands": Brand.query().order(Brand.name).fetch(),
        }
        self.response.write(template.render(template_var))

    def post(self, order_id, offer_id):
        name = self.request.get("name")
        desc = self.request.get("description")
        category = Category.get_by_id(int(self.request.get("category")))
        # status = self.request.get("status")
        brand = Brand.get_by_id(int(self.request.get("brand")))
        # img = self.request.get("photo", None)
        product = Product(name=name, description=desc, category=category, brand=brand)
        # product = Product(name=name, description=desc, category=category, brand=brand, img=img)
        # product.put()
        offer = Offer.get_by_id(int(offer_id))
        offer.products.append(product)
        offer.put()
        self.redirect("/order/" + order_id + "/offer/" + str(offer.key.id()))


class TradeAcceptHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write()

    def post(self, order_id, trade_id):
        trade = Trade.get_by_id(int(trade_id))
        trade_list = trade.query(Trade.order == order_id).fetch()
        for t in trade_list:
            if t.key.id() != trade.key.id():
                t.status = Trade.STATUS_REJECT
            else:
                t.status = Trade.STATUS_ACCEPT
                order = Order.get_by_id(order_id)
                order.status = Order.STATUS_INVALID
        trade.put()
        self.response.write()


class TradeRejectHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write()

    def post(self, trade_id):
        trade = Trade.get_by_id(int(trade_id))
        trade.status = Trade.STATUS_REJECT
        trade.put()
        self.response.write()


app = webapp2.WSGIApplication([
    ('/', HomepageHandler),
    ('/order/add', OrderRedirectHandler),  # change to /order/(\d+)/add, new Order before change page
    ('/order/(\d+)', OrderAddHandler),
    ('/order/(\d+)/view', OrderViewHandler),
    ('/order/(\d+)/product/add', ProductAddHandler),
    ('/(\d+)/orders', MyOrdersHandler),
    ('/order/(\d+)/offer/add', OfferRedirectHandler),
    ('/order/(\d+)/offer/(\d+)', OfferAddHandler),
    ('/order/(\d+)/offer/(\d+)/product/add', AddOfferProductHandler),
    ('/trade/(\d+)/offer/(\d+)/accept', TradeAcceptHandler),
    ('/trade/(\d+)/offer/(\d+)/reject', TradeRejectHandler),
], debug=True)
