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
print "<pre>"
print "<script>function abc(){location.href='/working.html'}</script>"
ss= commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+nameip+' sudo hadoop dfsadmin -report | head -10')
print "<b><font size='4'>"+ss+"</font></b>"
print "<button onclick='abc()'>BACK</button> "
print "\n\n"
print "</pre>"
