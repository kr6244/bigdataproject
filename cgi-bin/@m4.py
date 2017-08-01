#!/usr/bin/python2
import  cgi
import time
import commands
import os

print  "content-type:text/html"
print  ""
data=cgi.FieldStorage()
#print data
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
#user=int(data.getvalue('op'))
#ip=['192.168.10.102','192.168.10.103','192.168.10.122','192.168.10.104','192.168.10.109','192.168.10.171']
f=open('@ippu','r')
ip=f.read().splitlines()
f.close()
print ip
print '<h2><b>YOUR NAMENODE IS </b>:   '+ip[0]+'</h2>'
print '<br>'
j=0
print "<form name='gg' method='post' action='/cgi-bin/@m5.py' >"

#ip=['192.168.10.102','192.168.10.103','192.168.10.122','192.168.10.104','192.168.10.109','192.168.10.171']
for i in ip:
	j=j+1
	print '<div class="radio">'
	print j
	if(i==ip[0]):
		print "<b>Enter the name of directory of namenode</b>("+i+")&nbsp&nbsp:&nbsp<label><input type='text' name="+str(j)+"><label><b></b></br>"
	else:
		print "<b>Enter the name of directory of datanode</b>&nbsp ("+i+")&nbsp&nbsp:&nbsp<label><input type='text' name="+str(j)+"><label><b></b></br>"
	print '</div>'
print "<input type ='submit' value='Submit'>"
print "</form>"
	


