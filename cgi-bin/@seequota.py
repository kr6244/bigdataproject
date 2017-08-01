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
print "<pre>"
print "<b><font size='4'>the uploaded files and directories are </font></b>"
#ss= commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+nameip+' sudo hadoop fs -lsr /')
ss=commands.getoutput(" sudo ssh -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem ec2-user@"+pi+' sudo -i hdfs fs -lsr /')
print "<b><font size ='4'>"+ss+"</font></b>"
print "</pre>"
print '<form name ="ad" action ="/cgi-bin/@seequota2.py"  method="post">'
print '<font color="red"><b>ENTER DIRECTORY LOCATION</b></font> <input type="text" name="dirloc">'
print '<input type="submit" value ="submit" >'
print "</form>"


