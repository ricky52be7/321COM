from google.appengine.ext import ndb


class Category(ndb.Model):
    name = ndb.StringProperty()

    @classmethod
    def get_or_create(cls, name):
        category = cls.query().filter(cls.name==name).get()
        if category is not None:
            return category
        else:
            key = Category(name=name).put()
            return cls.get_by_id(key.id())

