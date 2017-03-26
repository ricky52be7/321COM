This is a Coventry University Project written in Python with GAE and Jinja2<br/>
features in it. The main aims of it is providing a trading platform for people<br/>
to exchange there electronical parts that doesn't need anymore.<br/>
<br/>
Web-map:<br/>
Homepage,Browsing orders for everyone<br/>
|-Sign Up<br/>
|-Login In<br/>
|   |-Add selling Order<br/>
|   |-Checking trading status of your Orders<br/>
|   |   |-Reject the offer<br/>
|   |   |-Accept the offer<br/>
|   |       |-Giving trade details after confirmed trade<br/>
|   |-View any Orders<br/>
|       |-Leaving Comments in Order<br/>
|       |-Giving Offer to the Order<br/>
|       |-Modify your posted offer<br/>
|-CMS Login<br/>
    |-Administrate on member accounts<br/>
    |-Administrate on member orders<br/>
    |-Administrate on member offers<br/>
    |-Administrate on member comments<br/>
    <br/>
    <br/>
Most of the data are constructed by GAE's ndb model and Jinja2 providing html<br/>
environment integration. Python written different classmethod for sending data<br/>
to the server.<br/>