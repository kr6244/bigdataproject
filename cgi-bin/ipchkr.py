#!/usr/bin/python2
import os
import time
import  commands
import cgi
print "Content-type:text/html"
print ""

l=[]
dict={}
f=open('automaticips','w')
for  i  in  range(226)[100: ]  :
	
	x=os.system('arping  -I br0  -c 1  192.168.10.'+str(i) +'&>/dev/null')
	
	if x == 0:
		l.append( "192.168.10."+str(i))
		ss=commands.getoutput( 'cat /proc/meminfo | head -1 | cut -d" " -f9')
		p=int(ss)		
		st="192.168.10."+str(i)
		dict[p]=st
		f.write(st)
		f.write('\n')


f.close()
a=dict.keys()
a.sort(reverse=True)


nameip=dict[a[0]]

f=open('namenodeip','w')
f.write(nameip)
f.close()
execfile('hdfsautomatic.py')


