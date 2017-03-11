from google.appengine.ext import ndb


class Account(ndb.Model):
    id = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)

    @classmethod
    def get_by_google_id(cls, google_id):
        return cls.query().filter(cls.id == google_id).get()
