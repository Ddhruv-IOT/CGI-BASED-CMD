# RHEL 8 system files and folders (Linux)

# Overview:
This directory contains files that are to be hosted on RHEL 8 using Apache Server.
<br> It has one folder linux_shell and 1 file named linux.jpg.
<br> The linux_shell directory is the backend.

# Setting Up 
- Linux_shell directory should be in CGI-BIN dir of Apache server.
- linux.jpg should be in Htdocs dir of Apache Server.
- after doing the above, navigate to the Linux_shell folder and make both files executable.
- to make files executable give the following command:
  > chmod +x \<file name>

# Notes: 
- CGI should be enabled on the Apache server.
- The backend files should be executable.
- The VM should have internet connectivity (use bridged adapter)
