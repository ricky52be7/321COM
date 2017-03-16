from google.appengine.ext import ndb


class Account(ndb.Model):
    id = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)

    @classmethod
    def get_by_google_id(cls, google_id):
        return cls.query().filter(cls.id == google_id).get()

    # use it to get and create account
    @classmethod
    def get_or_create(cls, uid, name):
        account = cls.query().filter(cls.id == uid, cls.name == name).get()
        if account is not None:
            return account
        else:
            key = Account(id=uid, name=name).put()
            return cls.get_by_id(key.id())
