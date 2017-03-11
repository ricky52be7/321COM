from google.appengine.ext import ndb


class Category(ndb.Model):
    name = ndb.StringProperty()
    description = ndb.TextProperty()
    category = ndb.StructuredProperty(Category, repeated=True)
    brand = ndb.StructuredProperty(Brand, repeated=True)
    create_at = ndb.DateTimeProperty(auto_now_add=True)
    update_at = ndb.DateTimeProperty(auto_now=True)
    status = ndb.IntegerProperty(1)  # status 1 = available, 2 = sold out, 3 = hide, 4 = delete