#! C:/Users/ACER/anaconda3/python.exe

import cgi
import subprocess as sp
import time
from sys import stdout
import vm_launcher


print("content-type: text/html")
print()
	


if __name__ == "__main__":

	data = cgi.FieldStorage()

	u_i = data.getvalue("system_name")

	if u_i == "Windows 10":
		print("""<meta http-equiv="refresh" content="0;url=/cgi-bin/cgi_cmd_files/windows_cgi_cmd.py" /> """)

	else:
		x = sp.getoutput("vboxmanage list runningvms")

		if "REHL8 Clone" in x:
			print("""<meta http-equiv="refresh" content="0;url=http://192.168.1.208/cgi-bin/doccmd.py?z=date" /> """)
	
		else:
			z = sp.getoutput("""vboxmanage startvm "REHL8 Clone" """)
			
			print(vm_launcher.vm_launcher_page)

			print("""<meta http-equiv="refresh" content="120;url=http://192.168.1.208/cgi-bin/doccmd.py?z=date" /> """)	##debug 
			
			if ("Waiting" and "started") in z:
				print("status: successful")

			else:
				print("status: failed")
