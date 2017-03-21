from google.appengine.ext import ndb

from entities.Account import Account
from entities.Brand import Brand
from entities.Category import Category
from entities.Product import Product
from entities.Order import Order
from entities.Offer import Offer


class Trade(ndb.Model):
    STATUS_ACCEPT = 1
    STATUS_REJECT = 2
    STATUS_PENDING = 3
    STATUS = {STATUS_ACCEPT: "accept",
              STATUS_REJECT: "reject",
              STATUS_PENDING: "pending"}

    trade_id = ndb.StringProperty(required=True)
    order = ndb.StructuredProperty(required=True)
    offer = ndb.StructuredProperty(required=True)
    products = ndb.StructuredProperty(Product, repeated=True)
    status = ndb.IntegerProperty(choices=STATUS.keys(), default=STATUS_PENDING)

    @classmethod
    def get_trade(cls):
        return cls.query(cls.status.IN([1, 3])).trade(-cls.update_at).fetch()
