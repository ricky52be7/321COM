from google.appengine.ext import ndb

from entities.Brand import Brand
from entities.Category import Category


class Product(ndb.Model):
    TYPES = ['Phone', 'Computer', 'Home Video Game Console', 'Audio', ]

    PHONE_CATEGORIES = ['', 'Mobile Phone', 'SmartPhone', '123']

    COMPUTER_CATEGORIES = ['', 'CPU', 'Power Supply Unit', 'Motherboard', 'Scanner/Printer', 'Mouse/Keyboard',
                           'Harddisk', 'Web Cam', 'Chassis', 'Display Card', 'Internal DVD Writer', 'RAM', 'RAID Card',
                           'Sound Card']

    HOME_GAME_CATEGORIES = ['']

    AUDIO_CATEGORIES = ['']

    COMPUTER_BRANDS = ['', 'AMD', 'INTEL', 'VIA', 'AMD', 'ASUS', 'AXLE', 'BioStar', 'Callbre', 'MSI', 'ASUS', 'BenQ',
                       'HP', 'LG', 'SamSung', 'DELL', 'Fujitsu', 'IBM', 'TOSHIBA', 'AsRock', 'ASUS', ]

    PHONE_BRANDS = ['Apple', 'Asus', 'HTC', 'Huawei', 'Lenovo', 'LG', 'Microsoft', 'Nokia', 'Samsung', 'Sony',
                    'BlackBerry']

    HOME_GAME_BRANDS = ['Sony', 'Microsoft', 'Nintendo']

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
    category = ndb.StructuredProperty(Category)
    brand = ndb.StructuredProperty(Brand)
    create_at = ndb.DateTimeProperty(auto_now_add=True)
    update_at = ndb.DateTimeProperty(auto_now=True)
    status = ndb.IntegerProperty(choices=STATUS.keys(), default=STATUS_AVAILABLE)

    @classmethod
    def get_by_id(cls, product_id):
        return cls.query().filter(cls.id == product_id).get()

    @classmethod
    def get_available_list(cls):
        return cls.query().filter(cls.status == 1).fetch()

    @classmethod
    def get_admin_list(cls):
        return cls.query(cls.status != 3).fetch()
