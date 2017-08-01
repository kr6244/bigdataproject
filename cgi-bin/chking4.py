#!/usr/bin/python
import cgi 
import os
import commands

print "Content-type:text/html"
print ""
ii='192.168.10.120'
print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no "+ii+' yum  install ftp://192.168.10.120/pub/jdk-7u79-linux-x64.rpm -y')
print "<b>hello</b>
	
