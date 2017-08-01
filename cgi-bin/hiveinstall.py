#!/usr/bin/python2
import os
import time
import  commands
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
<title> node startup
</title>
</head>
</html>
'''
print x
print "<b><center><font size='4'><u>INSTALLING HIVE</u></font></center></b><br><br>"
f=open('namenodeip','r')
nameip= f.readline()
f.close()

commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+nameip+' sudo  wget ftp://192.168.122.1/pub/apache-hive-1.2.2-bin.tar.gz')
commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+nameip+' sudo tar -xvzf apache-hive-1.2.2-bin.tar.gz')
print commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+nameip+'  sudo cp -r /root/apache-hive-1.2.2-bin  /hive')
commands.getoutput("sshpass -p 'q' sudo scp -o StrictHostKeyChecking=no  /root/.bashrc  root@"+nameip+":/root/")
print commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+nameip+'  sudo hadoop fs -chmod 777 /tmp')
commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+nameip+'  sudo hadoop fs -mkdir /tmp/hive')
print commands.getoutput("sshpass -p 'q' ssh -tt -o StrictHostKeyChecking=no root@"+nameip+'  sudo hadoop fs -chmod 777 /tmp/hive')


print "<b>everything is done!!!!!!</b><br><br>"
time.sleep(600)


print "<meta http-equiv = REFRESH CONTENT=1;url=/cgi-bin/hivequery1.py>"


