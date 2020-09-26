#! /pyt/python

import cgi
import subprocess as sp
import time
from sys import stdout


print("content-type: text/html")
print()
	


if __name__ == "__main__":
	data = cgi.FieldStorage()

	u_i = data.getvalue("system_name")

	if u_i == "Windows 10":
		print("""<meta http-equiv="refresh" content="0;url=/cgi-bin/f.py" /> """)

	else:
		x = sp.getoutput("vboxmanage list runningvms")
		#print(x)

		if "REHL8" in x:
			print("""<meta http-equiv="refresh" content="0;url=http://192.168.1.208/cgi-bin/doccmd.py?z=date" /> """)
	
		else:
			z = sp.getoutput("vboxmanage startvm REHL8") #IVR")
			
			print("""<meta name="viewport" content="width=device-width, initial-scale=1">
				 <h1><p> Kindly wait! we are launching the VM.</h1>
				 <h2><p>Time left</p>
				 <p id = "ti">time left</p></h2>
				 <div class="item4"><h3>The time now is: <p id="p4">TIME</p> and date: <p id="p5">dht</p></h3></div>
				 <script>
	var tlf = 120;
					function tm()
        					{
        						
							var d=new Date();
        						var h= d.getHours();
       		 					var m= d.getMinutes();
        						var s=d.getSeconds();
       							var d1=d.getDate();
        						var m1=d.getMonth();
        						var y1=d.getYear();
        						var a1=m1+1;
        						var e1=y1+1900;
        						document.getElementById("p4").innerHTML= h+":"+m+":"+s;
        						document.getElementById("p5").innerHTML= d1+":"+a1+":"+e1;
							document.getElementById("ti").innerHTML= tlf ;
        						document.getElementById("p4").style.color="red";
        						document.getElementById("p5").style.color="DarkMagenta";
							if (tlf > 0){
							tlf = tlf - 1;
							}
         					}
      
        				var x= setInterval(tm,1000);
				
				</script>
					<style>body 
    {
     background-color: rgb(180,180,200);
      font-family:Open Sans;
      overflow:hidden;
      height: 100vh;
      width: 80vw;
    }</style>""")
			
				

			
			print("""<meta http-equiv="refresh" content="120;url=http://192.168.1.208/cgi-bin/doccmd.py?z=date" /> """)	
			
			if ("Waiting" and "started") in z:
				print("status: successful")

			else:
				print("status: failed")



	
