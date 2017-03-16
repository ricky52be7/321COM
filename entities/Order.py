from google.appengine.ext import ndb

from entities.Account import Account


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
    description = ndb.TextProperty()
    user = ndb.StructuredProperty(Account, required=True)
    product_ids = ndb.IntegerProperty(repeated=True)
    create_at = ndb.DateTimeProperty(auto_now_add=True)
    update_at = ndb.DateTimeProperty(auto_now=True)
    status = ndb.IntegerProperty(default=STATUS_PENDING)
