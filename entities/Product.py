from google.appengine.ext import ndb


class Product(ndb.Model):
    CATEGORIES = ['', 'Test']
    BRANDS = ['', 'Test']
    STATUS_AVAILABLE = 1
    STATUS_SOLD = 2
    STATUS_HIDE = 3
    STATUS_DELETED = 4
    STATUS = {STATUS_AVAILABLE: "available",
              STATUS_SOLD: "sold out",
              STATUS_HIDE: "hide",
              STATUS_DELETED: "deleted"}

    name = ndb.StringProperty(required=True)
    description = ndb.TextProperty()
    category = ndb.StringProperty(choices=CATEGORIES)
    brand = ndb.StringProperty(choices=BRANDS)
    create_at = ndb.DateTimeProperty(auto_now_add=True)
    update_at = ndb.DateTimeProperty(auto_now=True)
    status = ndb.IntegerProperty(choices=STATUS.keys(), default=STATUS_AVAILABLE)
    # status 1 = available, 2 = sold out, 3 = hide, 4 = delete

    @classmethod
    def get_by_id(cls, product_id):
        return cls.query().filter(cls.id == product_id).get()

    @classmethod
    def get_available_list(cls):
        return cls.query().filter(cls.status == 1).get()

    @classmethod
    def get_admin_list(cls):
        return cls.query(cls.status != 3).get()
