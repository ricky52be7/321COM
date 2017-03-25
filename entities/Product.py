from google.appengine.ext import ndb

from entities.Brand import Brand
from entities.Category import Category

class Product(ndb.Model):
    name = ndb.StringProperty(required=True)
    description = ndb.TextProperty()
    category = ndb.StructuredProperty(Category)
    brand = ndb.StructuredProperty(Brand)
    img = ndb.BlobProperty(required=False)
    create_at = ndb.DateTimeProperty(auto_now_add=True)
    update_at = ndb.DateTimeProperty(auto_now=True)
    comment = ndb.TextProperty()