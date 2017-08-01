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
f=open('@dataipinstance','w')
nd=int(data.getvalue('nd'))
print '<pre>'

for i in range(0,nd):
	kk= commands.getoutput('sudo aws ec2 run-instances --image-id ami-f9ada180 --count 1 --instance-type t2.micro --key-name 2ndjune --security-groups launch-wizard-5 --query "Instances[0].InstanceId"')
	print kk
	f.write(kk)
	f.write('\n')
f.close()
print '</pre>'
print '<div class="container">'
print '<form method="post" action="/cgi-bin/@m3.py">'
print '<label>'
print '<input type="submit" value="Click to Configure!!">'
print '</label>'
print '</form>'
print '</div>'





