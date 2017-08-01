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
f=open('@ippu','r')
ip=f.read().splitlines()
print  ip
pi=ip[0]
data=cgi.FieldStorage()
loc=data.getvalue('dirloc')
print "<pre>"
print "<script>function abc(){location.href='/working2.html'}</script>"
#ss= commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+nameip+' sudo hadoop fs -count -q  '+loc)
ss= commands.getoutput(" sudo ssh -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem ec2-user@"+pi+' sudo -i  hdfs fs -count -q '+loc)

print "<b><font size ='4'>"+ss+"</font></b>"
print "</pre>"
print "\n\n"

print "<button onclick='abc()'>BACK</button> "

