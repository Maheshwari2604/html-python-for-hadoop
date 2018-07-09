#!/usr/bin/python2
import cgi
import commands
import os

print "Content-type:text/html"
print ""

form_data = cgi.FieldStorage()

#if(form_data.getvalue('file')):
#	file = form_data.getvalue('file')
#	print ("creating image")	
#	os.system("sudo cd /var/lib/libvirt/images")
#	os.system("sudo qemu-img create -f qcow2 -b rhvmdnd.qcow2 " + file + ".qcow2")

'''if(form_data.getvalue('VM')):
	VM = form_data.getvalue('VM')
	print ("Creating Virtual Machine")
	os.system("sudo virt-install --name " + VM + " --ram 512 --vcpu 1 --disk path=/var/lib/libvirt/images/"+ file +".qcow2 --import")'''

if(form_data.getvalue('nn12')):
	print ("Opening Namenode")
	commands.getoutput('sudo virsh start nn12')
	
if(form_data.getvalue('dn1')):
	print "Opening Datanode"
	commands.getoutput("sudo virsh start dn1")

if(form_data.getvalue('dn2')):
	print "Opening Datanode"
	commands.getoutput("sudo virsh start dn2")

if(form_data.getvalue('dn3')):
	print "Opening Datanode"
	commands.getoutput("sudo virsh start dn3")

if(form_data.getvalue('nn1')):
	print ("Destroying Namenode")
	commands.getoutput('sudo virsh destroy nn12')
	
if(form_data.getvalue('dn11')):
	print "Destroying Datanode"
	commands.getoutput("sudo virsh destroy dn1")

if(form_data.getvalue('dn22')):
	print "Destroying Datanode"
	commands.getoutput("sudo virsh destroy dn2")

if(form_data.getvalue('dn33')):
	print "Destroying Datanode"
	commands.getoutput("sudo virsh destroy dn3")

