#!/usr/bin/python
import cgi
import os
import time
import  commands
print "context-type:text/html"
print ""

data=cgi.FieldStorage()
nameip=data.getvalue('ip')
print nameip


print  "Loading  file for Hadoop HDFS Setup !!"

time.sleep(2)

ip=['192.168.10.122','192.168.10.128','192.168.10.102']
print  ip
print "\n"
#tip=raw_input("enter IP for Name Node  : ")
print '<font color="red"><b>name node directory name</b></font> <input type="text" name="namenode">'
 
data2=cgi.FieldStorage()
d=data2.getvalue('namenode')
c=0
for ii in ip :		
	# installing JDK
	print "\n"	
	#print "_______________________________________________________________________________________________"
	print "INSTALLING JDK FOR ip :  "+ii

	print ii
	
	commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no "+ii+' yum  install  /root/Desktop/jdk-7u79-linux-x64.rpm -y')
	
	
	#commands.getoutput('ssh  root@'+ii+' yum  install  /root/Desktop/jdk-7u79-linux-x64.rpm -y')

	#  Installing  Hadoop 
	print "\n"	
	#print "_______________________________________________________________________________________"
	print "INSTALLING HADOOP FOR ip :  "+ii
	commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no "+ii+'  rpm -ivh  /root/Desktop/hadoop-1.2.1-1.x86_64.rpm 	--replacefiles')
	
	#commands.getoutput('ssh  root@'+ii+'  rpm -ivh  /root/Desktop/hadoop-1.2.1-1.x86_64.rpm --replacefiles')
	
	#  setting  JAVA PATH
	print "SETTING JAVA PATH FOR ip :  "+ii
	commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no "+ii+' scp /root/.bashrc  root@'+ii+':/root/')
	print "\n"
	#print "______________________________________________________________________________________"
	
	#commands.getoutput('scp /root/.bashrc  root@'+ii+':/root/')
	print "\n"	
	#print "______________________________________________________________________________________"
	print "SETTING CORE-SITE.XML FOR IP :  "+ii
	
	# setting  core-site.xml 
	x='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this 	file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://'+nameip+':10001</value>\n</property>\n</configuration>'
        f=open('/tmp/core-site.xml','w')
	f.write(x)
	f.close()
	
	commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no "+ii+' scp   /tmp/core-site.xml   root@'+ii+':/etc/hadoop/core-site.xml')
	#commands.getoutput('scp   /tmp/core-site.xml   root@'+ii+':/etc/hadoop/core-site.xml')


	#  configure  hdfs-site.xml for  namenode 

y='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/'+d+'</value>\n</property>\n</configuration>'
f=open('/tmp/hdfs-site.xml','w')
f.write(y)
f.close()
print "\n"
#print "_______________________________________________________________________________________________"
print "SETTING HDFS-SITE FOR IP  :  "+nameip
commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no "+nameip+' scp   /tmp/hdfs-site.xml   root@'+nameip+':/etc/hadoop/hdfs-site.xml')


#commands.getoutput('scp   /tmp/hdfs-site.xml   root@'+nameip+':/etc/hadoop/hdfs-site.xml')
print "\n"
#print "_______________________________________________________________________________________________"
print "STARTING NAMENODE FOR IP  :  "+nameip

commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no "+nameip+' hadoop namenode  -format')
#commands.getoutput('ssh  root@'+nameip+' hadoop namenode  -format')

commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no "+nameip+' hadoop-daemon.sh start  namenode')
#commands.getoutput('ssh  root@'+nameip+' hadoop-daemon.sh start  namenode')

commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no "+nameip+' jps')
#commands.getoutput('ssh  root@'+nameip+' jps')


#for client node
ip2=ip

ll=-1
mn=0
for pp in ip :
	ll=ll+1
	u=ip[ll]
	if (u==nameip):
		mn=ll
		break


ip.pop(mn)
print "THE REMAINING IP ARE "
print "\n"
print ip2
print "\n"
'''
it=raw_input("enter ip for client node : ")
st=raw_input("do you want to change the default replication factor (3) and default block size (64mb) : (enter yes or  no )  :  ")
if st=='yes' :
	r1=raw_input("what do you want the default replication factor to be :  ")
	r2=raw_input("what do you want the default block size to be :  ")

	#  configure  hdfs-site.xml for  client ip
	y='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.replication</name>\n<value>/'+r1+'</value>\n</property>\n<property>\n<name>dfs.block.size</name>\n<value>/'+r2+'</value>\n</property>\n</configuration>'
	

	f=open('/tmp/hdfs-site.xml','w')
	f.write(y)
	f.close()
	
	print "\n"
	#print "_______________________________________________________________________________________________"
	print "SETTING HDFS-SITE FOR IP  :  "+it
	commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no "+it+' scp   /tmp/hdfs-site.xml   root@'+it+':/etc/hadoop/hdfs-site.xml')
	#commands.getoutput('scp   /tmp/hdfs-site.xml   root@'+it+':/etc/hadoop/hdfs-site.xml')

else :
	
	print "\n"
	#print "_______________________________________________________________________________________________"
	print "the default replication factor is 3 and block size is 64 mb "
	print "\n"	
	
'''
#  setting  up  data  node IPS  

'''
dnip=ip.remove(nameip)
print  "remaining IPs  are  :  ",dnip
'''


#print "_______________________________________________________________________________________________"
print "\n"
print   "plz wait for a moment  we are making  requirement for data node "
time.sleep(2)

ll2=-1
mn2=0
for pp2 in ip2 :
	ll2=ll2+1
	uu=ip2[ll2]
	if (uu==it):
		mn2=ll2
		break


ip2.pop(mn2)	
print ip2

for j in ip2 :
	
	print "\n"
	#print "_____________________________________________________________________________________"
	print"configuring hdfs file for ip and setting up data node :  "+j
	print "\n"
	
	#print  "setting up  datanode  : "
	dnd=raw_input("enter  directory name for  data node : ")
	#  creating  datanode  hdfs-site.xml 
	z='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this 	file. -->\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/'+dnd+'</value>\n</property>\n</configuration>'
	f=open('/tmp/hdfsdn-site.xml','w')	
	f.write(z)
	f.close()
	print "\n"
	#print "__________________________________________________________________________________"
	print "SETTING HDFS-SITE FOR IP  :  "+j
	print "\n"
	commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no "+j+' scp   /tmp/hdfsdn-site.xml   root@'+j+':/etc/hadoop/hdfs-site.xml')
	
	#commands.getoutput('scp   /tmp/hdfsdn-site.xml   root@'+j+':/etc/hadoop/hdfs-site.xml')
	print "\n"	
	#print "_________________________________________________________________________________"
	print "STARTING DATANODE FOR IP  :  "+j
	print "\n\n"
	commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no "+j+' hadoop-daemon.sh start  datanode')
	
	#commands.getoutput('ssh  root@'+j+' hadoop-daemon.sh start  datanode')
	
	commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no "+j+' jps')
	#commands.getoutput('ssh  root@'+j+' jps')	


print "everything is done!!!!!!"

#execfile('krproj2.py')
	

