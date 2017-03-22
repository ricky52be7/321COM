from google.appengine.ext import ndb

from entities.Account import Account
from entities.Brand import Brand
from entities.Category import Category
from entities.Product import Product


class Offer(ndb.Model):

    name = ndb.StringProperty(required=True)
    name_lower = ndb.ComputedProperty(lambda self: self.name.lower())
    description = ndb.TextProperty()
    user = ndb.StructuredProperty(Account, required=True)
    products = ndb.StructuredProperty(Product, repeated=True)
    create_at = ndb.DateTimeProperty(auto_now_add=True)
    update_at = ndb.DateTimeProperty(auto_now=True)

   # @classmethod
   # def get_my_order(cls):
   #     return cls.query(cls.status == 1).order(-cls.update_at).fetch()

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
                    if (product.category == category or category is None)\
                            and (product.brand == brand or brand is None)\
                            and (product.name in name or not name)\
                            and (order.name in name or not name):
                        result.append(order)
        return result

   # @classmethod
   # def sort_status(cls):
   #     return cls.query(cls.status == 1).order(-cls.update_at)

   # @classmethod
   # def search_name(cls, name_key):
   #     return cls.query(cls.name == name_key, cls.status == 1).order(-cls.update_at)

    @classmethod
    def search_name_lc(cls, name_key):
        name_key = name_key.lower()
        limit = name_key[:-1] + chr(ord(name_key[-1]) + 1)
        return cls.query(Offer.name_lower >= name_key, Offer.name_lower < limit).fetch(50)
