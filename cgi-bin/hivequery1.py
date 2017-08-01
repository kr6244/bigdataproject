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

print '<font size ="5"> ENTER YOUR QUERY :</font>'
print '<br><br>'

print '<font color="red" size ="5"><textarea rows="10" cols="50" name="dirloc"  form="ad" placeholder="enter"></textarea></font>'

print "<pre>"
print "<script>function abc(){location.href='/page2.html'}</script>"
print '<form id ="ad" action ="/cgi-bin/hivequery2.py"  method="post">'

print '<br>'
#print '<font color="red"><b>ENTER THE NO OF FILES ALLOWED IN THAT DIRECTORY</b></font> <input type="text" name="number">'
#print '<br>'
print '<input type="submit" value ="submit" >'
print "</form>"
print "\n"

print "<button onclick='abc()'>BACK</button> "
print "</pre>"


