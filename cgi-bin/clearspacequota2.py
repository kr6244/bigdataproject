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

print "<pre>"
print "<script>function abc(){location.href='/working.html'}</script>"
ss= commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+nameip+' sudo hadoop dfsadmin -clrSpaceQuota  '+loc)
print "<b><font size ='4'>"+ss+"</font></b>"
print "to see quota ---------"
print "\n\n"
print "CLICK BACK BUTTON --> GO TO SEE-QUOTA"
print "\n\n"
print "<button onclick='abc()'>BACK</button> "
print "</pre>"




