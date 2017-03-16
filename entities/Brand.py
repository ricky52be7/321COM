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

    @classmethod
    def seed(cls):
        Brand.get_or_create("")
        Brand.get_or_create("Apple")
        Brand.get_or_create("Asus")
        Brand.get_or_create("HTC")
        Brand.get_or_create("Huawei")
        Brand.get_or_create("Lenovo")
        Brand.get_or_create("LG")
        Brand.get_or_create("Microsoft")
        Brand.get_or_create("Nokia")
        Brand.get_or_create("Samsung")
        Brand.get_or_create("Sony")
        Brand.get_or_create("BlackBerry")
        Brand.get_or_create("Nintendo")
        Brand.get_or_create("AMD")
        Brand.get_or_create("INTEL")
        Brand.get_or_create("VIA")
        Brand.get_or_create("ASUS")
        Brand.get_or_create("AXLE")
        Brand.get_or_create("BioStar")
        Brand.get_or_create("Callbre")
        Brand.get_or_create("MSI")
        Brand.get_or_create("BenQ")
        Brand.get_or_create("HP")
        Brand.get_or_create("LG")
        Brand.get_or_create("DELL")
        Brand.get_or_create("Fujitsu")
        Brand.get_or_create("IBM")
        Brand.get_or_create("TOSHIBA")
        Brand.get_or_create("AsRock")
        Brand.get_or_create("Other")
