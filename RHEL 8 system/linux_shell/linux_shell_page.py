menu_page = """

<!DOCTYPE html>

	<html>
		<head>
			<title>LINUX CONTROL PANEL</title>
			<meta name="viewport" content="width=device-width, initial-scale=1">
		</head>

		<body>
			<div class = "form1">
				<form action = '/cgi-bin/linux_shell/linux_cgi_shell.py' >
					<h2 style="color: WHITE"> Enter your command here </h2>
					<input type = 'text' name = 'z' id = 'num1' placeholder = "command" id = "b1" list="exampleList"/>
						<datalist id="exampleList">
							<option value="date">  
	  						<option value="ifconfig">
							<option value="ls">  
	  						<option value="cal">
							<option value="gedit">  
			  				<option value="dd">
							<option value="pwd">  
			  				<option value="whoami">
							<option value="mkdir<dir_name>">  
			  				<option value="cheese&">
							<option value="firefox&">  
			  				<option value="echo <you want to display >">
							<option value="espeak-ng <text>">  
			  				<option value="systemctl status httpd">
							<option value="tree">
							<option value="nslookup">  
			  				<option value="vim">
			  				<option value="traceroute">  
			  				<option value="netstat">
						</datalist>
						<br/>
						<br/>
					<input type = 'submit' id = "b2"/>
				</form>
			</div>

			<style type="text/css">
				body
				{ 
					background-color: rgb(200,200,200);
				    background-image:url("/linux.jpg");
				    background-size: cover;
 	     			font-family:Open Sans;
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
"""
