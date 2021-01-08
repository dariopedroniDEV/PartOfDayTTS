# Constantly printed real time. Seems to be 0.5S behind the machine clock.
from datetime import datetime
now = datetime.now()
import time
while True:
    time.sleep(0.2)
    test = datetime.now()
    current_time = test.strftime("%H:%M:%S")
    print("\r" + str(current_time), end="")
    #print("Test \r")