#!/usr/bin/python2
import os
import time
import  commands
import cgi
print "Content-type:text/html"
print ""
data=cgi.FieldStorage()

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
print "<b><center><font size='4'><u>STARTING THE CLUSTER</u></font></center></b><br><br>"
print  "<b>Loading  file for Hadoop HDFS Setup !! </b><br><br>"

#nameip='192.168.122.146'
f=open('namenodeip','r')
nameip= f.readline()
f.close()


f=open('ips','r')
ip= f.read().splitlines()
f.close()

dict={}
cc=0
for i in ip:
	cc=cc+1
	print i
	ss="dataname"+str(cc)
	
	t1=data.getvalue(ss)
	dict[i]=t1
	print dict[i]
	print t1
print('\n')
print len(nameip)
print dict
d=dict[nameip]


'''
print  ip
print "\n"
tip=raw_input("enter IP for Name Node  : ")
nameip=tip
d=raw_input("enter  meta data directory name :  ")
'''
c=0
for ii in ip :		
	print ii
	# installing JDK
	print "\n"	
	#print "_______________________________________________________________________________________________"
	print "<b>INSTALLING JDK FOR ip :  "+ii+"</b><br><br>"

	
	
	print commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+ii+' sudo yum  install ftp://192.168.122.1/pub/jdk-7u79-linux-x64.rpm -y')
	
	
	#commands.getoutput('ssh  root@'+ii+' yum  install  /root/Desktop/jdk-7u79-linux-x64.rpm -y')

	#  Installing  Hadoop 
	print "\n"	
	#print "_______________________________________________________________________________________"
	print "<b>INSTALLING HADOOP FOR ip :  "+ii+"</b><br><br>"
	print commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+ii+' sudo  rpm -ivh  ftp://192.168.122.1/pub/hadoop-1.2.1-1.x86_64.rpm 	--replacefiles')
	
	#commands.getoutput('ssh  root@'+ii+'  rpm -ivh  /root/Desktop/hadoop-1.2.1-1.x86_64.rpm --replacefiles')
	
	#  setting  JAVA PATH
	print "<b>SETTING JAVA PATH FOR ip :  "+ii+"</b><br><br>"
	commands.getoutput("sshpass -p 'q' sudo scp -o StrictHostKeyChecking=no  /root/.bashrc  root@"+ii+":/root/")
	print "\n"
	#print "______________________________________________________________________________________"
	
	#commands.getoutput('scp /root/.bashrc  root@'+ii+':/root/')
	print "\n"	
	#print "______________________________________________________________________________________"
	print "<b>SETTING CORE-SITE.XML FOR IP :  "+ii+"</b><br><br>"
	
	# setting  core-site.xml 
	x='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this 	file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://'+nameip+':10001</value>\n</property>\n</configuration>'
        f=open('/tmp/core-site.xml','w')
	f.write(x)
	f.close()
	
	commands.getoutput("sshpass -p 'q' sudo scp -o StrictHostKeyChecking=no /tmp/core-site.xml  root@"+ii+":/etc/hadoop/core-site.xml")
	#commands.getoutput('scp   /tmp/core-site.xml   root@'+ii+':/etc/hadoop/core-site.xml')


	#  configure  hdfs-site.xml for  namenode 

y='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/'+d+'</value>\n</property>\n</configuration>'
f=open('/tmp/hdfs-site.xml','w')
f.write(y)
f.close()
print "\n"
#print "_______________________________________________________________________________________________"
print "<b>SETTING HDFS-SITE FOR IP  :  "+nameip+"</b><br><br>"
commands.getoutput("sshpass -p 'q' sudo scp -o StrictHostKeyChecking=no  /tmp/hdfs-site.xml   root@"+nameip+":/etc/hadoop/hdfs-site.xml")


#commands.getoutput('scp   /tmp/hdfs-site.xml   root@'+nameip+':/etc/hadoop/hdfs-site.xml')
print "\n"
#print "_______________________________________________________________________________________________"
print "<b>STARTING NAMENODE FOR IP  :  "+nameip+"</b><br><br>"

commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+nameip+' sudo  hadoop namenode  -format')
#commands.getoutput('ssh  root@'+nameip+' hadoop namenode  -format')

commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+nameip+' sudo hadoop-daemon.sh start  namenode')
#commands.getoutput('ssh  root@'+nameip+' hadoop-daemon.sh start  namenode')

commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+nameip+' sudo jps')
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
#print "THE REMAINING IP ARE "
#print "\n"
#print ip2
#print "\n"
#it=raw_input("enter ip for client node : ")
'''
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
print   "<b>plz wait for a moment  we are making  requirement for data node</b> <br><br>"

'''
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
'''

for j in ip2 :
	
	print "\n"
	#print "_____________________________________________________________________________________"
	print"<b>configuring hdfs file for ip and setting up data node :  "+j+"</b><br><br>"
	print "\n"
	
	#print  "setting up  datanode  : "
	#dnd=raw_input("enter  directory name for  data node : ")
	#  creating  datanode  hdfs-site.xml 
	dnd=dict[j]
	z='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this 	file. -->\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/'+dnd+'</value>\n</property>\n</configuration>'
	f=open('/tmp/hdfsdn-site.xml','w')	
	f.write(z)
	f.close()
	print "\n"
	#print "__________________________________________________________________________________"
	print "<b>SETTING HDFS-SITE FOR IP  :  "+j+"</b><br><br>"
	print "\n"
	commands.getoutput("sshpass -p 'q' sudo scp -o StrictHostKeyChecking=no   /tmp/hdfsdn-site.xml   root@"+j+":/etc/hadoop/hdfs-site.xml")
	
	#commands.getoutput('scp   /tmp/hdfsdn-site.xml   root@'+j+':/etc/hadoop/hdfs-site.xml')
	print "\n"	
	#print "_________________________________________________________________________________"
	print "<b>STARTING DATANODE FOR IP  :  "+j+"</b><br><br>"
	print "\n\n"
	commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+j+' sudo hadoop-daemon.sh start  datanode')
	
	#commands.getoutput('ssh  root@'+j+' hadoop-daemon.sh start  datanode')
	
	commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+j+' sudo jps')
	#commands.getoutput('ssh  root@'+j+' jps')	


print "<b>everything is done!!!!!!</b><br><br>"

print "<meta http-equiv = REFRESH CONTENT=1;url=/working.html>"
	

