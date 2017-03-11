from google.appengine.ext import ndb

from entities.Account import Account


class Order(ndb.Model):
    name = ndb.StringProperty(required=True)
    description = ndb.TextProperty()
    user = ndb.StructuredProperty(Account, required=True)
    product_ids = ndb.IntegerProperty(repeated=True)
    create_at = ndb.DateTimeProperty(auto_now_add=True)
    update_at = ndb.DateTimeProperty(auto_now=True)
    status = ndb.IntegerProperty(default=1)  # status 1 = available, 2 = sold out, 3 = hide, 4 = delete
