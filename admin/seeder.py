import webapp2

from entities.Brand import Brand
from entities.Category import Category

"""
    TYPES = ['Phone', 'Computer', 'Home Video Game Console', 'Audio', ]

    PHONE_CATEGORIES = ['', 'Mobile Phone', 'SmartPhone', '123']

     COMPUTER_CATEGORIES = ['', 'CPU', 'Power Supply Unit', 'Motherboard', 'Scanner/Printer', 'Mouse/Keyboard',
                           'Hard Disk', 'Web Cam', 'Chassis', 'Display Card', 'Internal DVD Writer', 'RAM', 'RAID Card',
                          'Sound Card']

    HOME_GAME_CATEGORIES = ['']

    AUDIO_CATEGORIES = ['']

    COMPUTER_BRANDS = ['', 'AMD', 'INTEL', 'VIA', 'AMD', 'ASUS', 'AXLE', 'BioStar', 'Callbre', 'MSI', 'BenQ',
                       'HP', 'LG', 'SamSung', 'DELL', 'Fujitsu', 'IBM', 'TOSHIBA', 'AsRock', ]

    PHONE_BRANDS = ['Apple', 'Asus', 'HTC', 'Huawei', 'Lenovo', 'LG', 'Microsoft', 'Nokia', 'Samsung', 'Sony',
                    'BlackBerry']

    HOME_GAME_BRANDS = ['Sony', 'Microsoft', 'Nintendo']
    """


class CategorySeederHandler(webapp2.RequestHandler):
    def get(self):
        Category.seed()
        self.response.write("finish")


class BrandSeederHandler(webapp2.RequestHandler):
    def get(self):
        Brand.seed()
        self.response.write("finish")


class SeederHandler(webapp2.RequestHandler):
    def get(self):
        Category.seed()
        Brand.seed()
        self.response.write("finish")


app = webapp2.WSGIApplication([
    ('/seeding/category', CategorySeederHandler),
    ('/seeding/brand', BrandSeederHandler),
    ('/seeding/all', SeederHandler),
], debug=True)
