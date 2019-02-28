##################################################################
#This script is use to test the tnsping status of CRMPROD database  
#for both node
##################################################################


#Importing packages 

from subprocess import Popen,PIPE
import subprocess

#command for first node tnsping

tnsstring1=["tnsping","(DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = svhj2029-vip)(PORT = 1910)) (ADDRESS = (PROTOCOL = TCP)(HOST = svhj2029-vip)(PORT = 1911)) (ADDRESS = (PROTOCOL = TCP)(HOST = svhj2029-vip)(PORT = 1912)) (ADDRESS = (PROTOCOL = TCP)(HOST = svhj2029-vip)(PORT = 1913)) (LOAD_BALANCE = yes) (CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = CRMPROD)))","10"]

out=Popen(tnsstring1,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

print("TNSping status for node svhj2029-vip\n")
print(out.communicate()[0])


#Command for second node tnsping

tnsstring2=["tnsping","(DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = svhj2030-vip)(PORT = 1910)) (ADDRESS = (PROTOCOL = TCP)(HOST = svhj2030-vip)(PORT = 1911)) (ADDRESS = (PROTOCOL = TCP)(HOST = svhj2030-vip)(PORT = 1912)) (ADDRESS = (PROTOCOL = TCP)(HOST = svhj2030-vip)(PORT = 1913)) (LOAD_BALANCE = yes) (CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = CRMPROD)))","10"]

out=Popen(tnsstring2,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

print("TNSping status for node svhj2030-vip\n")
print(out.communicate()[0])

