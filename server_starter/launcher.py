import subprocess as sp
import threading as t
import webbrowser
import time
import os

def ipAdd():
    global e
    x = sp.getoutput("""netsh interface ip show address \"Wi-Fi\" | findstr \"IP Address\" """).strip().split()
    e = x[2]
    print("Your Current IP address: {}".format(e))

def server1():
    print("Starting ------> Server")
    st_output = sp.getstatusoutput("httpd.exe")
    if st_output != 0:
        print("Error Contact Admin")

def chrome1():
    webbrowser.open("http://{}:8080/windows_cmd_frontend/select.html".format(e))

if __name__ == "__main__":

    try:
        ipAdd()
        t.Thread(target=server1).start()
        time.sleep(5)
        print("Launching -----> Chrome")
        time.sleep(5)
        t.Thread(target=chrome1).start();
        
        while 1:
            user_input = input("Type cmd to start command prompt")
            os.system(user_input)

    except Exception as e:
        print("Error: ", e)
        
