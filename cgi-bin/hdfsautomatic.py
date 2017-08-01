#!/usr/bin/python
import cgi 
import os
import commands
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
<head>
'''
print x

f=open('namenodeip','r')
nameip=f.readline()
f.close()

print '<b><center><font size="5"><u>your namenode is :  '+ nameip+'</u></font></center></b>' 
print '<br><br><br>'

f=open('automaticips','r')
ipp= f.read().splitlines()
f.close()


#ipp=['192.168.122.146','192.168.122.1']
c=0
print '<form name ="ad" action ="/cgi-bin/setting2.py"  method="post">'


for q in ipp:
	c=c+1
	ss="dataname"+str(c)
	
	
	if q==nameip:
		print '<font color="blue" size="4"><b>ENTER META-DIRECTORY NAME FOR NAMENODE : </b></font>'+'<b><font size="4">'+ q +'</b></font>'+'&nbsp &nbsp &nbsp&nbsp &nbsp &nbsp&nbsp;'+'<input type="text" name="'+ ss +'">'
		print '<br><br>'
	else :
		print '<font color="blue" size="4"><b>ENTER META-DIRECTORY NAME FOR DATANODE : </b> </font>'+'<b><font size="4">'+ q +'</b></font>' 			+ '&nbsp&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp;'+'<input type="text" name="'+ ss +'">'
		print '<br><br>' 

print '<br><br>'
print '&nbsp &nbsp &nbsp &nbsp'
print '<input type="submit" value ="submit">'
print '</form>'



