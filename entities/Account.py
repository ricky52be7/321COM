from google.appengine.ext import ndb


class Account(ndb.Model):
    id = ndb.IntegerProperty()
