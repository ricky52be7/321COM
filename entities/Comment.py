from google.appengine.ext import ndb

from entities.Account import Account


class Comment(ndb.Model):
    # cmid = ndb.IntegerProperty(required=True) # use ndb id instead of custom id
    # order_id = ndb.IntegerProperty(required=True)  # use structuredProperty in Order rather than build relation
    user = ndb.StructuredProperty(Account, required=True)
    comment = ndb.TextProperty(required=True)
    create_at = ndb.DateTimeProperty(auto_now_add=True)
    update_at = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def get_related_comment(cls):
        return cls.query(cls.orderid).order(-cls.create_at).fetch()
