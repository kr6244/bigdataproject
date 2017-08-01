#!/usr/bin/python
import cgi
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
</html>
'''
print x

data=cgi.FieldStorage()
val=data.getvalue('selection')


if val=='manual':
	print '<b><center><font size ="6" color="blue"><u>LIST OF IP</u><font></center></b><br><br>'
	print '<b><font size ="4" color="blue">SELECT NAMENODE IP</font></b><br><br>'
	print  '<form name ="ac" action ="/cgi-bin/hdfsmanual.py"  method="post">'
	f=open('ips','r')
	ip= f.read().splitlines()
	f.close()

	for q in ip :
		 print '<input type="radio" name="ip" value='+q+'> <b><font size="3">'+q+'<font></b><br><br>'

	print '<input type="submit" value ="submit">'	
	print '</form>'

		
else :
 	execfile('ipchkr.py')
        
