#!/usr/bin/python

import sys, getopt



linecount=''
type=''
file=''


def err():
	print("Usage: %s -n linecount [-type [log|console] -name outputfilename]" % sys.argv[0])
	sys.exit(2)


try:
    myopts, args = getopt.getopt(sys.argv[1:],"n:t:l:")
except getopt.GetoptError as e:
    print (str(e))
    err()
    #print("Usage: %s -n linecount [-type [log|console] -name outputfilename]" % sys.argv[0])

 
for o, a in myopts:
    if o == '-n':
        linecount=a
    elif o == '-t':
        type=a
    elif o == '-l':
	file1=a

head=''
if type is not None:
	if (type == "console"):
		   with open("apache_log.log") as myfile:
                        head = myfile.readlines(int(linecount))
                        print head
	elif (type == "log" and file1 is not None):
		with open("apache_log.log") as myfile:
       			head = myfile.readlines(int(linecount))
		with open(file1,'a') as log_file:
        	 	log_file.write(str(head)+"\n")
	else:
		err()
		



