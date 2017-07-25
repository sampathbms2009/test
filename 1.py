#!/usr/bin/python

iplist=[]
for line in open('apache_log.log').readlines():
	ips=line.split()[0]
	iplist.append(ips)

getcount=deletecount=putcount=postcount=0
for ip in set(iplist):
        for line in open('apache_log.log'):
		if ip in line:
			if 'GET' in line:
				getcount+=1 
			elif 'PUT' in line:
				putcount+=1
			elif 'POST' in line:
				postcount+=1
			elif 'DELETE' in line:
				deletecount+=1
	print str(ip) + ": GET="+str(getcount)+" PUT="+str(putcount)+" DELETE=" +str(deletecount) + " POST=" + str(postcount)

