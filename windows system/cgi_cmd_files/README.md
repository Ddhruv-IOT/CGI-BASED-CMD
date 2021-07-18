# Information About files

## System_selector file:
- it selects the system based on user input from the frontend
- if the input is Windows OS, then it redirects to windows_cgi_cmd.py
- if the input is RHEL-8 then: 
    > - if RHEL 8 is already working, then it will connect to VM using its IP address.
    > - else RHEL 8 will be launched and then it will connect to VM.
- For getting VM IP Guest Additions are used.

## vm_launcher file:
- It is used with System_selector.py
- It is used to display the time remaining when the VM is launched behind the scene.

## windows_cgi_cmd file:
- It is used to process commands given to windows
- It uses win_cmd_page.py to display the list of available options.

## win_cmd_page:
- It contains the menu from windows cmd.

## Config.py
- It only controls the "delay" across all the files.
- value of delay = 300
- delay is used to give time to Vm to boot properly and connect to network.

# New Features:
- Added Threading support.
- dynamically update IP address of VM and base OS.
- Empty input and Error handling.
- changed file structure.
- Removed extra files and code.
