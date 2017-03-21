from google.appengine.ext import ndb

from entities.Account import Account
from entities.Brand import Brand
from entities.Category import Category
from entities.Product import Product


class Order(ndb.Model):
    STATUS_AVAILABLE = 1
    STATUS_SOLD = 2
    STATUS_HIDE = 3
    STATUS_DELETED = 4
    STATUS_PENDING = 5
    STATUS = {STATUS_AVAILABLE: "available",
              STATUS_SOLD: "sold out",
              STATUS_HIDE: "hide",
              STATUS_DELETED: "deleted",
              STATUS_PENDING: "pending"}

    name = ndb.StringProperty(required=True)
    name_lower = ndb.ComputedProperty(lambda self: self.name.lower())
    description = ndb.TextProperty()
    user = ndb.StructuredProperty(Account, required=True)
    products = ndb.StructuredProperty(Product, repeated=True)
    create_at = ndb.DateTimeProperty(auto_now_add=True)
    update_at = ndb.DateTimeProperty(auto_now=True)
    status = ndb.IntegerProperty(choices=STATUS.keys(), default=STATUS_PENDING)

    @classmethod
    def get_my_order(cls):
        return cls.query(cls.status.IN([1, 2, 5])).order(-cls.update_at).fetch()

    @classmethod
    def search(cls, name, category_id, brand_id):
        orders = cls.query().fetch()
        result = []
        for order in orders:
            if order.name in name:
                result.append(order)
            else:
                for product in order.products:
                    category = Category.get_by_id(category_id) if category_id else None
                    brand = Brand.get_by_id(brand_id) if brand_id else None
                    if (product.category == category or category is None) \
                            and (product.brand == brand or brand is None) \
                            and (product.name in name or not name)\
                            and (order.name in name or not name):
                        result.append(order)
        return result

    @classmethod
    def sort_status(cls):
        return cls.query(cls.status == 1).order(-cls.update_at)

    @classmethod
    def search_name(cls, name_key):
        return cls.query(cls.name == name_key, cls.status == 1).order(-cls.update_at)

    @classmethod
    def search_name_lc(cls, name_key):
        name_key = name_key.lower()
        limit = name_key[:-1] + chr(ord(name_key[-1]) + 1)
        return cls.query(Order.name_lower >= name_key, Order.name_lower < limit).fetch(50)
