#!/usr/bin/python2
import  cgi
import time
import commands
import os

print  "content-type:text/html"
print  ""
data=cgi.FieldStorage()
print data
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
f=open('@ippu','r')
ip=f.read().splitlines()
print  ip
pi=ip[0]
u1=data.getvalue('1')
u2=data.getvalue('2')
u3=data.getvalue('3')
u4=data.getvalue('4')
print u1
print pi
#print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+pi+" sudo fallocate -l "+u3+"M "+u1)
#print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+pi+" sudo fallocate -l "+u3+"M "+u1)
print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+pi+" sudo hadoop fs -Ddfs.replication="+u3+" -Ddfs.block.size="+u4+"  -put "+u1+" "+u2)
print '<form method="post" action="/working2.html">'
print '<label><input type="submit" value="Click to perform more"></label>'
print '</form>'





