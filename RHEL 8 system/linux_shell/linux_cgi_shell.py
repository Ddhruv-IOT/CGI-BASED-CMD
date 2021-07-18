#! /usr/bin/python3
# C:/Users/ACER/anaconda3/python.exe

import cgi 
import subprocess
import threading as t
import linux_shell_page as lsp

print("context-type: text/html")
print()

def server1():
	
	output = subprocess.getoutput(f"sudo {usr_input}")
	print("""<pre><h2 style="color: WHITE">Your Output = {}</h2></pre>""".format(output))

print(lsp.menu_page)

if __name__ == "__main__":
	
	try:
		data = cgi.FieldStorage()
		usr_input = data.getvalue("z")

		if usr_input != None:
			t.Thread(target = server1).start()
			print("""<pre><h2 style="color: WHITE">Your Input = sudo {}</h2></pre>""".format(usr_input))

		else:
			print("""<pre><h2 style="color: WHITE">Welcome Give some input to start. </h2></pre>""")
	
	except Exception as e:
		print("An error occured", e)