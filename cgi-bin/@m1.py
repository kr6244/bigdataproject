#!/usr/bin/python

import  cgi
import time
import commands
import os

print  "content-type:text/html"
print  ""
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
<title> namenode instance
</title>
</head>
</html>
'''
print x
print '<pre>'
#f=open('i','w')
#f.write( commands.getoutput('sudo aws ec2 describe-instances | grep PublicIpAddress | grep -o -P "\d+\.\d+\.\d+\.\d+" | grep -v "^10\."'))
#print commands.getoutput('sudo aws ec2 describe-instances --region us-west-2 --output table')
#print commands.getoutput('sudo aws ec2 describe-instances | grep PublicIpAddress | grep -o -P "\d+\.\d+\.\d+\.\d+" | grep -v "^10\."')
#print commands.getoutput('aws ec2 run-instances --image-id ami-6f68cf0f --count 1 --instance-type t2.micro --key-name 2ndjune --security-group-ids launch-wizard-5 --region us-west-2')
#f.close()
kk= commands.getoutput('sudo aws ec2 run-instances --image-id ami-09939f70 --count 1 --instance-type t2.micro --key-name 2ndjune --security-groups launch-wizard-5 --query "Instances[0].InstanceId" ')
f=open('@nameipinstance','w')
f.write(kk)
f.close()
print '</pre>'
print '<div class="container">'
print '<form method="post" action="/@data1.html">'
print '<label>'
print '<input type="submit" value="Click to Start the creation of Data nodes!!">'
print '</label>'
print '</form>'
print '</div>'


















