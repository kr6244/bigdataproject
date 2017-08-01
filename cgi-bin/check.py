#!/usr/bin/python
import cgi
print "Content-type:text/html"
print ""

data=cgi.FieldStorage()
user=data.getvalue('fname')
passd=data.getvalue('sname')
ww='''
<html>
<body>hello
<meta http-equiv = REFRESH CONTENT=1;url=/mayank.html>
</body>
</html>
'''
e='''
<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>

<div class="container">

       
 <script>
 alert("WRONG PASSWORD !")</script>
 <meta http-equiv = REFRESH CONTENT=0;url=/index.html>

</div>

</body>
</html>
'''
if user=='kaushik' and passd=='12345' :
	print "<meta http-equiv = REFRESH CONTENT=0;url=/loading.html>"
else :
	print e

