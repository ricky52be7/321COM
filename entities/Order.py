from google.appengine.ext import ndb

from entities.Offer import Offer


class Order(Offer):
    STATUS_ACCEPTED = 6
    STATUS_REJECTED = 7
    Offer.STATUS['STATUS_ACCEPTED'] = "accepted"
    Offer.STATUS['STATUS_REJECTED'] = "rejected"

    olist = ndb.StructuredProperty(Offer, required=True)

    @classmethod
    def post_reply(cls):
        if()
