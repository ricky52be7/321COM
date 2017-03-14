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

    @classmethod
    def seed(cls):
        Category.get_or_create("")
        Category.get_or_create("Mobile Phone")
        Category.get_or_create("CPU")
        Category.get_or_create("Power Supply Unit")
        Category.get_or_create("Motherboard")
        Category.get_or_create("Scanner / Printer")
        Category.get_or_create("Mouse / Keyboard")
        Category.get_or_create("Hard Disk")
        Category.get_or_create("Web Cam")
        Category.get_or_create("Chassis")
        Category.get_or_create("Display Card")
        Category.get_or_create("Internal DVD Writer")
        Category.get_or_create("RAM")
        Category.get_or_create("RAID Card")
        Category.get_or_create("Sound Card")
        Category.get_or_create("Other")
