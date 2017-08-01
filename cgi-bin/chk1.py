#!/usr/bin/python
import cgi
import os
import time
import  commands
print "context-type:text/html"
print ""

data=cgi.FieldStorage()
nameip=data.getvalue('ip')

print "<b>"+nameip+"</b>"
