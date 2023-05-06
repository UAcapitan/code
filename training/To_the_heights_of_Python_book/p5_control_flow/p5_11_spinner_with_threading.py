import sys
import time
import itertools
import threading


class Signal:
    go = True

def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush

    for char in itertools.cycle("|/-\\"):
        status = f"{char} {msg}"
        write(status)
        flush()
        write("\x08" * len(status))
        time.sleep(.1)
        if not signal.go:
            write("\x08" * len(status))
            write(" " * len(status))  
            write("\x08" * len(status))       
            break


if __name__ == "__main__":
    signal = Signal()
    spinner = threading.Thread(target=spin, args=("Processing", signal))

    spinner.start()
    time.sleep(1)
    signal.go = False
    spinner.join()
    print("Finished")  
