#!/usr/bin/python
import cgi
import commands
import time ,os
print "Content-type:text/html"
print ""
data=cgi.FieldStorage()

f=open('namenodeip','r')
nameip= f.readline()
f.close()
loc=data.getvalue('pic')
print commands.getoutput("sshpass -p 'q' sudo scp -o StrictHostKeyChecking=no "+ loc +' root@'+nameip+":/") 
print "<meta http-equiv = REFRESH CONTENT=0;url=/working.html>"


