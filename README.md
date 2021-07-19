# CGI BASED CMD

## OVERVIEW:

In this fast world everyone wants to save time, be more productive and no one wants to remember big commands or equation,
everyone prefers to google it rather than remembering it. 
<br/> As I am also a human, same applies to me, I don't like to remember CLI commands but at the same time, I also know that how important they are for a CSE student.
<br/>So to deal with this situation WEB based CMD is created.

In this web based cmd I had make a dropdown list from where you can select the command.
<br/>Hence you can use the command also and you don't have to remember it or google it.

I have developed this using CGI scripting for both Windows and RHEL 8. 

We can start the CMD in our base OS and from that we can control our base OS i.e. Windows and also control RHEL8 from the same.
<br/> Even we can control both the OS from our mobile also.

I had tried to made it dynamic and automated i.e 
<br/> on single click the CGI - based - CMD for windows will open.
<br/> no need to remember ip address, code will automatically update it.

If we choose OS to be RHEL 8, so the code will automatiaclkly connect to vm,
<br/> we dont need to manullay go and start the vm code will do it automaticcly.
<br/> Also ip of vm will be updated automatically

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
<br/> On single click, the server will be launched, browser will open automaticcaly
and will ask on which system would you like to work.
<br/> I have chosen Windows 10.

[Link to Video - Part 1](https://youtu.be/EtJRetCNOM4)

### Case II:
In this case, I have chosen RHEL8 as my OS and will run some command on it using web based cmd
<br/> Here, RHEL8 was already running.

[Link to Video - Part 2](https://youtu.be/1_QpEwFUy1o)

### Case III:
In this case again, I have selected RHEL 8 as my OS but this time, its not already turned on.
<br/> In this case my code will automatically start the vm, it takes 2-3 mins till the time a waiting page will be displayeda
<br/> after that i can run my commands

[Link to Video - Part 3](https://youtu.be/EoMdKkjeNLo)

## Detailed Article:
[Link to Article](https://www.linkedin.com/feed/update/urn:li:ugcPost:6715690477959614464?updateEntityUrn=urn%3Ali%3Afs_feedUpdate%3A%28*%2Curn%3Ali%3AugcPost%3A6715690477959614464%29)

## Prequisties:

## New Updates:

## Future scope:
- More commands can be added.
- Can be made more dynamic and easy to setup 
- Artificial Intelligence can be added to provide the functionality to find the apps installed on OS and automatically add them to the menu.
- For Security purposes, Authentication can be added, as anyone can connect to our ip and can run any  command, which can be really hazerdeous. 
- Moving the whole project to Flask Server
 
 ## Notes and known issues:
 - This app works only on Windows.
 - To launch an app from this app, the path is required to be set in env. var.
 - The app will stop or hang when it launches apps like chrome.

# Thank You
