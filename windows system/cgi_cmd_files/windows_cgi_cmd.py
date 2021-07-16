#! C:/Users/ACER/anaconda3/python.exe

import cgi
import subprocess
import threading as t
import win_cmd_page as page

print("content-type: text/html")
print()

def server1():
	
	output = subprocess.getoutput(usr_input)
	print("""<pre><h2 style="color: WHITE">Your Output ={}</h2></pre>""".format(output))

print(page.cmd_page)

if __name__ == "__main__":
	data = cgi.FieldStorage()
	usr_input = data.getvalue("num1")

	if usr_input != None:
		t.Thread(target = server1).start()
		print("""<pre><h2 style="color: WHITE">Your Input = {}</h2></pre>""".format(usr_input))

	else:
		print("""<pre><h2 style="color: WHITE">Welcome Give some input to start. </h2></pre>""")