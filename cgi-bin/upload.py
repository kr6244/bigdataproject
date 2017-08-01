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
f=open('/var/www/html/works.txt','r')
loc=f.read().splitlines()
f.close()
print "<pre>"
print "<script>function abc(){location.href='/working.html'}</script>"
ss= commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+nameip+' sudo hadoop fs -Ddfs.replication='+loc[1] +'  -Ddfs.blocksize='+loc[2]+' -put '+loc[0]+ '  '+loc[3])
print "<b><font size ='4'>"+ss+"</font></b>"
print "<button onclick='abc()'>BACK</button> "
print "</pre>"
