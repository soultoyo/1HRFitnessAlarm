import time
import tkinter
from tkinter import messagebox


def main():
    # Setting up TKinter for the message box later, to appear once the timer has finished
    root = tkinter.Tk()
    root.call('wm', 'attributes', '.', '-topmost', True)
    root.withdraw()

    
    hour = 1
    minute = 0
    seconds = 0

    while 1:
        time.sleep(1)

        if seconds < 0:
            seconds = 59
            minute -= 1
            if minute < 0 and hour >= 0:
                minute = 59
                hour -= 1

        if hour < 0:
            break
        
        print_time_string(hour, minute, seconds)
        seconds -= 1

    # Display messagebox when time is up
    messagebox.showinfo(parent=root, title="Exercise time",
                        message="Time to do exercise!!!")

def print_time_string(hour, minute, seconds):
    # Zero padding for the time string so that if there is a single digit, the time will be padded with a zero first e.g. 1 -> 01
    seconds_string = str(seconds)
    if len(seconds_string) != 2:
        seconds_string = '0' + str(seconds)

    minute_string = str(minute)
    if len(minute_string) != 2:
        minute_string = '0' + str(minute)

    hour_string = str(hour)
    if len(hour_string) != 2:
        hour_string = '0' + str(hour)

    # The /r is to make sure the cursor on the console goes back to the beginning so we can update the current line
    print(hour_string + ":" + minute_string +
            ":" + seconds_string, end='\r', flush=True)


if __name__ == "__main__":
    main()
