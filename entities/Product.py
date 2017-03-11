from google.appengine.ext import ndb

from entities import Brand
from entities import Category


class Product(ndb.Model):
    name = ndb.StringProperty()
    description = ndb.TextProperty()
    category = ndb.StructuredProperty(Category)
    brand = ndb.StructuredProperty(Brand)
    create_at = ndb.DateTimeProperty(auto_now_add=True)
    update_at = ndb.DateTimeProperty(auto_now=True)
    status = ndb.IntegerProperty(1)  # status 1 = available, 2 = sold out, 3 = hide, 4 = delete

    STATUS_AVAILABLE = 1
    STATUS_SOLD = 2
    STATUS_HIDE = 3
    STATUS_DELETE = 4

    @classmethod
    def get_by_id(cls, product_id):
        return cls.query().filter(cls.id == product_id).get()

    @classmethod
    def get_available_list(cls):
        return cls.query().filter(cls.status == 1).get()

    @classmethod
    def get_admin_list(cls):
        return cls.query(cls.status != 3).get()
