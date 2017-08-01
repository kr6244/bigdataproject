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
no=data.getvalue('number')
print "<pre>"
print "<script>function abc(){location.href='/working2.html'}</script>"
#ss= commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+nameip+' sudo hadoop dfsadmin -setQuota '+no +' '+loc)
ss= commands.getoutput(" sudo ssh -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem ec2-user@"+pi+' sudo -i  hdfs dfsadmin -setQuota '+no +' '+loc)
print "<b><font size ='4'>"+ss+"</font></b>"
print "to see quota ---------"
print "\n\n"
print "CLICK BACK BUTTON --> GO TO SEE-QUOTA"
print "\n\n"

print "<button onclick='abc()'>BACK</button> "
print "</pre>"


