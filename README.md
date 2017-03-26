This is a Coventry University Project written in Python with GAE and Jinja2
features in it. The main aims of it is providing a trading platform for people
to exchange there electronical parts that doesn't need anymore.

Web-map:
Homepage,Browsing orders for everyone
|-Sign Up
|-Login In
|   |-Add selling Order
|   |-Checking trading status of your Orders
|   |   |-Reject the offer
|   |   |-Accept the offer
|   |       |-Giving trade details after confirmed trade
|   |-View any Orders
|       |-Leaving Comments in Order
|       |-Giving Offer to the Order
|       |-Modify your posted offer
|-CMS Login
    |-Administrate on member accounts
    |-Administrate on member orders
    |-Administrate on member offers
    |-Administrate on member comments
    
    
Most of the data are constructed by GAE's ndb model and Jinja2 providing html
environment integration. Python written different classmethod for sending data
to the server.