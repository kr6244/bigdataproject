#!/usr/bin/python
import cgi
import commands
import time ,os
print "Content-type:text/html"
print ""
x='''
<html>
<head>
<style>
table, th, td {
    border: 3px solid black;
}
body {
background-color : powderblue;
}
</style>
<title> node startup
</title>
</head>
</html>
'''
print x
f=open('namenodeip','r')
nameip= f.readline()
f.close()
data=cgi.FieldStorage()
loc=data.getvalue('dirloc')
f=open('commands','w')
f.write(loc)
f.close()

print "<pre>"
print "<script>function abc(){location.href='/cgi-bin/hivequery1.py'}</script>"
ss=commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+ nameip+"  hive  -f /var/www/cgi-bin/commands")
print "<b><font size ='4'>"+ss+"</font></b>"

print "\n\n"

print "<button onclick='abc()'>BACK</button> "
print "</pre>"



