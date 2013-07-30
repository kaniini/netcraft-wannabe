netcraft-wannabe
----------------

This is a simple DNS service that checks the Server header on a subdomain given to it.

It uses TortoiseLabs' JSONCB-based DNS API, which is kind of neat -- this API allows webapps to
directly control what DNS records are returned for it.

How it works is simple:

1. I have a JSONCB callback registered for netcraft.dereferenced.org, to an instance of this app
   using the builtin webserver, at http://turtle.dereferenced.org:5000
2. Nameservers pass queries as HTTP POST messages to http://turtle.dereferenced.org:5000 and we
   respond with the data.
3. The nameservers pass and cache our returned data back to the client.

This is a very basic example of what can be done with the JSONCB APIs, of course.  I just
built this because I was bored...

