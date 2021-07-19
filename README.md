# CGI BASED CMD

## OVERVIEW:

In this fast world, everyone wants to save time, be more productive and no one wants to remember big commands or equations,
everyone prefers to google it rather than remembering it. 
<br/> As I am also a human, the same applies to me, I don't like to remember CLI commands but at the same time, I also know that how important they are for a CSE student.
<br/>So to deal with this situation WEB based CMD is created.

In this web-based cmd, I had to make a dropdown list from where you can select the command.
<br/>Hence you can use the command also and you don't have to remember it or google it.

I have developed this using CGI scripting for both Windows and RHEL 8. 

We can start the CMD in our base OS and from that we can control our base OS i.e. Windows and also control RHEL8 from the same.
<br/> Even we can control both the OS from our mobile also.

I had tried to make it dynamic and automated i.e 
<br/> on a single click the CGI - based - CMD for windows will open.
<br/> no need to remember the IP address, code will automatically update it.

If we choose OS to be RHEL 8, so the code will automatically connect to VM,
<br/> we don't need to manually go and start the VM code will do it automatically.
<br/> Also IP of VM will be updated automatically

## Tools And Technologies Used:

> ### Languages Used:
- Python 3
- HTML
- CSS
- Java Script
- bash Script
- CGI Script

> ### Softwares Used: 
- Virtual Box
- Apache Server
- VIM, Gedit 
- Spyder, Vs Code

> ### OS Used:
- Windows 10 
- RHEL 8

## Demo Videos:

### Case I:
Here, I will be demonstrating the power of a single click.
<br/> On a single click, the server will be launched, the browser will open automatically, and will ask on which system would you like to work.
<br/> I have chosen Windows 10.

[Link to Video - Part 1](https://youtu.be/EtJRetCNOM4)

### Case II:
In this case, I have chosen RHEL8 as my OS and will run some commands on it using a web-based cmd
<br/> Here, RHEL8 was already running.

[Link to Video - Part 2](https://youtu.be/1_QpEwFUy1o)

### Case III:
In this case, again, I have selected RHEL 8 as my OS but this time, it's not already turned on.
<br/> In this case my code will automatically start the VM, it takes 2-3 mins till the time awaiting page will be displayed
<br/> after that I can run my commands

[Link to Video - Part 3](https://youtu.be/EoMdKkjeNLo)

## Detailed Article:
[Link to Article](https://www.linkedin.com/feed/update/urn:li:ugcPost:6715690477959614464?updateEntityUrn=urn%3Ali%3Afs_feedUpdate%3A%28*%2Curn%3Ali%3AugcPost%3A6715690477959614464%29)

## Prerequisites:
- Path of Virtual Box should be set. 
- CGI should be enabled.
- Path of python should be set.
- Both OS should be connected to LAN.
- VM should be in Bridged network mode.
- Guest additions should be added on VM.

## New Updates:
- Added Threading Support 
- Added Automatic IP address updater for both the OSs
- Removed redundant codes
- minor output bug fixes

## Future scope:
- More commands can be added.
- UI can be improved and can be made more intutive.
- Can be made more dynamic and easy to setup.
- Artificial Intelligence can be added to provide the functionality to find the apps installed on OS and automatically add them to the menu.
- For Security purposes, Authentication can be added, as anyone can connect to our IP and can run any command, which can be very hazardous. 
- Moving the whole project to Flask Server.
 
 ## Notes and known issues:
 - May cause security losses as no authentication system is added
 - Under development

# Some Outputs
## First page - System selector (Selected Windows)
![server op 1](https://user-images.githubusercontent.com/54676859/126180486-963cd25b-94d5-41fa-b391-c3c6b667a82b.png)

## Second Page - Running command on Windows System WEB CMD
![server op 2](https://user-images.githubusercontent.com/54676859/126180648-c71d1d0f-2bb3-4d52-a647-4c01eb615e5d.png)

## Third Page - System selector (Selected RHEL 8)
![server op 3](https://user-images.githubusercontent.com/54676859/126180749-55fb3e95-8bab-40f2-b10d-1d4c6b4b9c53.png)

## Fourth Page - VM being launched by code automatically
![server op 4](https://user-images.githubusercontent.com/54676859/126181088-aa085695-419e-49a3-9be4-427521de2a6b.png)

## Fifth Page - Running command on RHEL 8 System WEB CMD
![server op 6](https://user-images.githubusercontent.com/54676859/126181349-aa63fc4d-1b2d-440c-8fda-6d09818d1a47.png)
 
# Thank You
