from google.appengine.ext import ndb


class Order(ndb.Model):
    name = ndb.StringProperty()
    description = ndb.TextProperty()
    create_at = ndb.DateTimeProperty(auto_now_add=True)
    update_at = ndb.DateTimeProperty(auto_now=True)
    status = ndb.IntegerProperty(default=1)  # status 1 = available, 2 = sold out, 3 = hide, 4 = delete
