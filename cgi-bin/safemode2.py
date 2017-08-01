#!/usr/bin/python
import cgi
import commands
import time
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
print "<script>function abc(){location.href='/working.html'}</script>"
print commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+nameip+' sudo hadoop dfsadmin -safemode leave')
print "\n\n"
print "<button onclick='abc()'>GO BACK</button> "
