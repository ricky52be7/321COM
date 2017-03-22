from google.appengine.ext import ndb

from entities.Order import Order
from entities.Offer import Offer


class Trade(ndb.Model):
    STATUS_ACCEPT = 1
    STATUS_REJECT = 2
    STATUS_PENDING = 3
    STATUS = {STATUS_ACCEPT: "accept",
              STATUS_REJECT: "reject",
              STATUS_PENDING: "pending"}
    # STATUS_AVAILABLE = 1
    # STATUS_SOLD = 2
    # STATUS_HIDE = 3
    # STATUS_DELETED = 4
    # STATUS_PENDING = 5
    # STATUS = {STATUS_AVAILABLE: "available",
    #           STATUS_SOLD: "sold out",
    #           STATUS_HIDE: "hide",
    #           STATUS_DELETED: "deleted",
    #           STATUS_PENDING: "pending"}

    order = ndb.IntegerProperty(required=True)
    offer = ndb.IntegerProperty(required=True)
    status = ndb.IntegerProperty(choices=STATUS.keys(), default=STATUS_PENDING)
    create_at = ndb.DateTimeProperty(auto_now_add=True)
    update_at = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def get_trade(cls):
        return cls.query(cls.status == 3).order(-cls.update_at).fetch()

    @classmethod
    def get_all(cls):
        return cls.query.order(-cls.update_at).fetch()