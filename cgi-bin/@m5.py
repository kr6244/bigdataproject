#!/usr/bin/python2
import  cgi
import time
import commands
import os

print  "content-type:text/html"
print  ""
data=cgi.FieldStorage()
print data
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
user=1
print user
l=str(user)
d=data.getvalue(l)
#ip=['192.168.10.102','192.168.10.103']
f=open('@ippv','r')
ip=f.read().splitlines()
f.close()
print  ip
f=open('@ippu','r')
ip1=f.read().splitlines()
f.close()
print  ip1

i=user
piu=ip1[user-1]
piv=ip[user-1]
print"namenode"
print piu
print piv
print d
print "<pre>"
for ik in ip1:
	# setting  core-site.xml 
	print "------------------------------------------SETTING CORE_SITE : "+ik+"-----------------------------------------------------"
	x='<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.defaultFS</name>\n<value>hdfs://'+piv+':10001</value>\n</property>\n</configuration>'

	f=open('/tmp/core-site.xml','w')
	f.write(x)
	f.close()
	print commands.getoutput(" sudo scp -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem  /tmp/core-site.xml  ec2-user@"+ik+":/hadoop2/etc/hadoop/core-site.xml  ")

print d	
#  configure  hdfs-site.xml for  namenode 
print "-------------------------------------------------SETTING HDFS_SITE : "+piv+"------------------------------------------------------"
y='<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.namenode.name.dir</name>\n<value>/'+d+'</value>\n</property>\n</configuration>'

print d
f=open('/tmp/hdfs-site.xml','w')
f.write(y)
f.close()
print d
print commands.getoutput(" sudo scp -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem /tmp/hdfs-site.xml ec2-user@"+piu+":/hadoop2/etc/hadoop/hdfs-site.xml")
print commands.getoutput(" sudo ssh -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem ec2-user@"+piu+' sudo -i hadoop namenode  -format')
print commands.getoutput(" sudo ssh -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem ec2-user@"+piu+' sudo -i hadoop-daemon.sh start  namenode')
print commands.getoutput(" sudo ssh -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem ec2-user@"+piu+' sudo -i jps')


#  setting  up  data  node IPS  

print   "-------------------------------plz wait for a moment  we are making  requirement for data node --------------------------------------"
#time.sleep(2)

dnip=ip1
'''
ll=-1
mn=0
for kk in ip:
	ll=ll+1
	u=ip[ll]
	if(u==pi):
		mn=ll
		break
ip.pop(mn)
print dnip
'''
print  "-----------------------------------------------------setting up  datanode  : -----------------------------------------------------"

#  creating  datanode  hdfs-site.xml
ll=1
print "user"
print user
for j in dnip:
	if(ll==user):
		ll=ll+1
	else:
		dnd=data.getvalue(str(ll))
		print dnd
		print "SETTING HDFS_SITE : "+j
		z='<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in thisfile. -->\n<configuration>\n<property>\n<name>dfs.datanode.data.dir</name>\n<value>/'+dnd+'</value>\n</property>\n</configuration>'
		f=open('/tmp/hdfsdn-site.xml','w')
		f.write(z)
		f.close()
		print commands.getoutput(" sudo scp -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem /tmp/hdfsdn-site.xml ec2-user@"+j+":/hadoop2/etc/hadoop/hdfs-site.xml")
		print commands.getoutput(" sudo ssh -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem ec2-user@"+j+' sudo -i hadoop-daemon.sh start datanode')
		print commands.getoutput(" sudo ssh -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem ec2-user@"+j+' sudo -i jps')
		ll=ll+1

print '</pre>'
print '<h2>CLUSTER SETUP SUCCESSFUL!!</h2>'
print '<form method="post" action="/working2.html">'
print '<div>'
print '<label><input type="submit" value="Click to start uploading files in cluster "></label>'
print '</div>'
print "<input type ='hidden' name='p' value="+str(user)+">"
print '</form>'













