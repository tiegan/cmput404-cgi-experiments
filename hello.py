#!/usr/bin/env python

# ^ this thing is called the "shebang"

import os
import json
import cgi

form = cgi.FieldStorage()

username = form.getvalue('user')
password = form.getvalue('password')

C = Cookie.SimpleCookie()
C.load(os.environ["HTTP_COOKIE"])

print "Content-Type: text/html"
if username == "mcdavid" and password == "isthebest":
    print "Cookie: loggedin=true"
else:
    print "Cookie: loggedin=false"
print # ^^^ HTTP ^^^     vvv HTML vvv
#print "\r\nHello World~*~"
print "<HTML><BODY>"
print "<H1>Hello World!</H1>"
print "Your magic trackig number is:"
print form.getvalue('magic_tracking_number')
print "<P>Your Browser is"

if "Firefox" in os.environ["HTTP_USER_AGENT"]:
    print "Firefox!"
elif "Chrome" in os.environ["HTTP_USER_AGENT"]:
    print "Chrome!"
else:
    #print "something I don't know!"
    print os.environ["HTTP_USER_AGENT"]

print "<FORM method='POST'><INPUT name='user'><INPUT name='password' type='password'>"
print "<INPUT type='submit'></FORM>"

print "<P>Username: " + str(username)
print "<P>Password: " + str(password)

if username == "mcdavid" and password == "isthebest":
    print "<P>Login successful!"
else:
    print "<P>You're a monster!"

#print "<P>" + json.dumps(dict(C, indent=2))
if 'loggedin' in C:
    print "<P>Logged in: " + str(C['loggedin'].value)
else:
    print "<P>No cookie"


#curl -A Fiefox localhost:8000/hello.py

#print json.dumps(dict(os.environ), indent=2, sort_keys=True)
