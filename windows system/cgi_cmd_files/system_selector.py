#! C:/Users/ACER/anaconda3/python.exe

import config
import cgi
from sys import stdout
import subprocess as sp
import time
import vm_launcher
import threading as t

delay = config.delay 

print("content-type: text/html")
print()

def vm_ip_fetch():
	global vm_ip
	time.sleep(delay-4)
	vm_ip = sp.getoutput("""VBoxManage guestproperty get "REHL8 Clone" "/VirtualBox/GuestInfo/Net/0/V4/IP" """)

def disp_output(message):
	print(f"<h2>{message}</h2>")
	stdout.flush()
	
if __name__ == "__main__":

	data = cgi.FieldStorage()

	usr_choice = data.getvalue("system_name")

	if usr_choice == "Windows 10":
		print("""<meta http-equiv="refresh" content="0;url=/cgi-bin/cgi_cmd_files/windows_cgi_cmd.py" /> """)

	else:
		vm_name = sp.getoutput("vboxmanage list runningvms")

		if "REHL8 Clone" in vm_name:

			vm_ip = sp.getoutput("""VBoxManage guestproperty get "REHL8 Clone" "/VirtualBox/GuestInfo/Net/0/V4/IP" """)
			print(f"""<meta http-equiv="refresh" content="0;url=http://{vm_ip.split(" ")[1]}/cgi-bin/doccmd.py?z=date" /> """)
	
		else:

			start_vm = sp.getoutput("""vboxmanage startvm "REHL8 Clone" """)
			t.Thread(target=vm_ip_fetch).start()
			
			disp_output(vm_launcher.vm_launcher_page)	
			time.sleep(delay + 2)
			disp_output(vm_ip)

			print(f"""<meta http-equiv="refresh" content="1;url=http://{vm_ip.split(" ")[1]}/cgi-bin/doccmd.py?z=date" /> """)

			if ("Waiting" and "started") in start_vm:
				disp_output("Status: successful")

			else:
				disp_output("Status: failed")

