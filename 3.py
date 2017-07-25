#!/usr/bin/python

import sys, getopt, commands, os

sourceurl=''
username=''
password=''


def err():
	print("Usage: %s -s <source url> -u <username> -p password]" % sys.argv[0])
	sys.exit(2)


try:
    myopts, args = getopt.getopt(sys.argv[1:],"s:u:p:")
except getopt.GetoptError as e:
    print (str(e))
    err()

 
for o, a in myopts:
    if o == '-s':
        sourceurl=a
    elif o == '-u':
        username=a
    elif o == '-p':
	password=a

currentversion = commands.getoutput("git ls-remote -t https://"+username+":"+password+"@"+sourceurl+"| awk -F'/' '{print $3}'| tail -n 1")
print "Current Version: "+ currentversion
version = str(int(currentversion.split("-v")[-1])+1)
updatedversion = (currentversion.split("-v")[-2]+"-v"+version)

commands.getoutput("git tag | xargs git tag -d")
commands.getoutput("git tag "+ updatedversion)
command = commands.getoutput("git push https://"+username+":"+password+"@"+sourceurl+" --tags")
print "Updated Version: "+updatedversion
