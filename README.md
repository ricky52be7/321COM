This is a Coventry University Project written in Python with GAE and Jinja2<br/>
features in it. The main aims of it is providing a trading platform for people<br/>
to exchange there electronical parts that doesn't need anymore.<br/>
<br/>
Web-map:<br/>
Homepage,Browsing orders for everyone<br/>
|-Sign Up<br/>
|-Login In<br/>
|&nbsp;&nbsp;&nbsp;&nbsp;|-Add selling Order<br/>
|&nbsp;&nbsp;&nbsp;&nbsp;|-Checking trading status of your Orders<br/>
|&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;|-Reject the offer<br/>
|&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;|-Accept the offer<br/>
|&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Giving trade details after confirmed trade<br/>
|&nbsp;&nbsp;&nbsp;&nbsp;|-View any Orders<br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Leaving Comments in Order<br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Giving Offer to the Order<br/>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-Modify your posted offer<br/>
|-CMS Login<br/>
&nbsp;&nbsp;&nbsp;&nbsp;|-Administrate on member accounts<br/>
&nbsp;&nbsp;&nbsp;&nbsp;|-Administrate on member orders<br/>
&nbsp;&nbsp;&nbsp;&nbsp;|-Administrate on member offers<br/>
&nbsp;&nbsp;&nbsp;&nbsp;|-Administrate on member comments<br/>
    <br/>
    <br/>
Most of the data are constructed by GAE's ndb model and Jinja2 providing html<br/>
environment integration. Python written different classmethod for sending data<br/>
to the server.<br/>