from google.appengine.ext import ndb

from entities.Order import Order
from entities.Account import Account


class Comment(ndb.model):
    cmid = ndb.IntegerProperty(required=True)
    orderid = ndb.IntegerProperty(Order.get_by_id, required=True)
    user = ndb.StructuredProperty(Account, required=True)
    title = ndb.StringProperty(required=True)
    description = ndb.TextProperty()
    create_at = ndb.DateTimeProperty(auto_now_add=True)
    update_at = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def get_related_comment(cls):
        return cls.query(cls.orderid).order(-cls.create_at).fetch()