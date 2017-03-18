from google.appengine.ext import ndb

from entities.Brand import Brand
from entities.Category import Category


class Product(ndb.Model):
    STATUS_AVAILABLE = 1
    STATUS_SOLD = 2
    STATUS_HIDE = 3
    STATUS_DELETED = 4
    STATUS = {STATUS_AVAILABLE: "available",
              STATUS_SOLD: "sold out",
              STATUS_HIDE: "hide",
              STATUS_DELETED: "deleted"}

    name = ndb.StringProperty(required=True)
    description = ndb.TextProperty()
    category = ndb.StructuredProperty(Category)
    brand = ndb.StructuredProperty(Brand)
    create_at = ndb.DateTimeProperty(auto_now_add=True)
    update_at = ndb.DateTimeProperty(auto_now=True)
    status = ndb.IntegerProperty(choices=STATUS.keys(), default=STATUS_AVAILABLE)

    @classmethod
    def get_available_list(cls):
        return cls.query().filter(cls.status == 1).fetch()

    @classmethod
    def get_admin_list(cls):
        return cls.query(cls.status != 3).fetch()

    @classmethod
    def get_order_products(cls, product_ids):
        return ndb.get_multi(product_ids)
