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
<title> datanode instance
</title>
</head>
</html>
'''
print x
a=open('@ippu','w')
b=open('@ippv','w')
f=open('@nameipinstance','r')
kk=f.read()
ss=kk[1:-1]
f.close()
print ss

nipu= commands.getoutput("sudo aws ec2 describe-instances --instance-ids "+ss+" --query 'Reservations[0].Instances[0].PublicIpAddress'")
nipv= commands.getoutput("sudo aws ec2 describe-instances --instance-ids "+ss+" --query 'Reservations[0].Instances[0].PrivateIpAddress'")
nipu=nipu[1:-1]
nipv=nipv[1:-1]
a.write(nipu)
b.write(nipv)
a.write('\n')
b.write('\n')
print nipu
print nipv

print '<h2><u><b> <span style="color:red">YOUR NAMENODE IS  </span></b></u> :- </h2>'
print '<h2>'
print nipu 
print '</h2>'
g=open('@dataipinstance','r')
dataip=g.read().splitlines()
g.close()
print dataip
print '<h2><u><b> <span style="color:red">YOUR DATANODES ARE </span></b></u>:-'
print '</h2>'
j=1;
for ii in dataip:
	ii=ii[1:-1]
	nipu= commands.getoutput("sudo aws ec2 describe-instances --instance-ids "+ii+" --query 'Reservations[0].Instances[0].PublicIpAddress'")
	nipv= commands.getoutput("sudo aws ec2 describe-instances --instance-ids "+ii+" --query 'Reservations[0].Instances[0].PrivateIpAddress'")
	nipu=nipu[1:-1]
	nipv=nipv[1:-1]
	a.write(nipu)
	b.write(nipv)
	a.write('\n')
	b.write('\n')
	print "<h2>"	
	print j
	print ")&nbsp&nbsp&nbsp&nbsp&nbsp"
	j=j+1
	print nipu
	print '</h2>'
a.close()
b.close()
f.close()


print '<div class="container">'
print '<br><br>'
print '<form method="post" action="/cgi-bin/@m4.py">'
print '<label>'
print '<input type="submit" value="Click to Set meta directories!!">'
print '</label>'
print '</form>'
print '</div>'



