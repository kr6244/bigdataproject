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
print '<form method="post" action="/cgi-bin/@uploading2.py">'
print '<b>Enter the name of file to upload :</b>'
print '<label><input type="text" name="1"></label>'
print '<br><b>Enter the location to upload: </b>'	
print '<label><input type="text" name="2"></label>'
print '<br><b>Enter the size of sample file to upload : </b>'	
print '<label><input type="text" name="3"></label>'
print '<br><b>Enter the replication size: </b>'	
print '<label><input type="text" name="4"></label>'
print '<br><b>Enter the block size in bytes : </b>'	
print '<label><input type="text" name="5"></label>'
print '<label><input type="submit" value="Click to set"></label>'
print '</form>'
