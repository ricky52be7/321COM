from google.appengine.ext import ndb


class Brand(ndb.Model):
    name = ndb.StringProperty()

    @classmethod
    def get_or_create(cls, name):
        brand = cls.query().filter(cls.name == name).get()
        if brand is not None:
            return brand
        else:
            key = Brand(name=name).put()
            return cls.get_by_id(key.id())
