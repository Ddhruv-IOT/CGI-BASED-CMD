#! /pyt/python

import cgi
import subprocess
import pyttsx3
import threading as t

print("content-type: text/html")
print()

def server1():
	ef = subprocess.getoutput(u_i)
	print("""<h2 style="color: WHITE">Your Output = {}</h2>""".format(ef))

print("""

<!DOCTYPE html>

	<html>
		<head>
			<title>CONTROL PANEL</title>
			<meta name="viewport" content="width=device-width, initial-scale=1">
		</head>

		<body>
			<div class = "form1">

			<form action = 'http://192.168.1.206/cgi-bin/f.py' >

				<h2 style="color: WHITE">Enter your command here</h2>
				<input type = 'text' name = 'num1' id = 'num1' placeholder = "command"/ id = "b1" list="exampleList">
				<datalist id="exampleList">
				<option value="date /t">  
  				<option value="time /t">
				<option value="VirtualDj8">  
  				<option value="Whatsapp">
				<option value="notepad">  
  				<option value="ping google.com">
				<option value="ipconfig">  
  				<option value="VirtualBox">
				<option value="vboxmanage list vms">  
  				<option value="vboxmanage list runningvms">
				<option value="chrome">  
  				<option value="cmd">
				<option value="spyder">  
  				<option value="dir">
				<option value="cls">  
  				<option value="hostname">
  				<option value="perfmon">  
  				<option value="route">
				</datalist>
				
				<br/>
				<br/>
				<input type = 'submit' id = "b2"/>
			</form>

			</div>

			<style type="text/css">
				body{ background-color: rgb(200,200,200);
				      background-image:url("/bg.jpg");
				      background-size: cover;
 	     			      font-family:Open Sans;
				      overflow:hidden;
				      height: 100vh;
				      width: 100vw;					
				      overflow-y:auto;
      				      height: 100vh;
      				      width: 80vw;
				    }

				form1
    				    { 
				      text-align: center;
				      text-decoration-color:green;
				      margin: auto;
				      width: 50vw;
				      height: 50vh;
				      position: absolute;
				      top:1vh;
				      bottom: 1vh;
				      left: 1vw;
				      right: 1vw;
				      margin: auto;
				      padding: 10vh;
   				    }
			</style>
		</body>
	</html>

""")





if __name__ == "__main__":
	ef = ' '
	global u_i
	data = cgi.FieldStorage()
	u_i = data.getvalue("num1")
	t1 = t.Thread(target = server1)
	t1.start();
	print("""<h2 style="color: WHITE">Your Input = {}</h2>""".format(u_i))
	#t1.join(10)