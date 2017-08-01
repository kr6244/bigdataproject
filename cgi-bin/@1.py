#!/usr/bin/python2
import  cgi

print  "Content-type:text/html"
print  ""


data=cgi.FieldStorage()
#print data
user=data.getvalue('firstname')

password=data.getvalue('lastname')
web='''
<html> 
<meta http-equiv=REFRESH CONTENT=1;url=/@2.html>
</html>
'''
qw='''
<html> 
<script> alert("WRONG CREDENTIALS")</script>
<meta http-equiv=REFRESH CONTENT=0;url=/@1.html>
</html>
'''
if  user == 'kaushik'  and  password  == '12345' :
        
        print  web
else :
        print   "ERROR PAGE !! "
	print    qw

