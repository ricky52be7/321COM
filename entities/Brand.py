from google.appengine.ext import ndb


class Brand(ndb.Model):
    name = ndb.StringProperty()
