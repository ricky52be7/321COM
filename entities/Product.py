from google.appengine.ext import ndb


class Product(ndb.Model):
    id = ndb.IntegerProperty()
