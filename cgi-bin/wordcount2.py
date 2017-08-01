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
inloc=data.getvalue('dirloc')
outloc=data.getvalue('space')
print "<pre>"
print "<script>function abc(){location.href='/mapreduce.html'}</script>"
ss= commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+nameip+' sudo hadoop jar /usr/share/hadoop/hadoop-examples-1.2.1.jar  wordcount '+ inloc +' '+outloc)


print "\n\n"
ss2= commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+nameip+' sudo hadoop fs -cat '+ outloc+ '/part-r-00000')
print "<b><font size ='4'>"+ss2+"</font></b>"

print "<button onclick='abc()'>BACK</button> "
print "</pre>"


