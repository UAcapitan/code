
import time
import os

def pusher():
    t = input("Time: ")
    commands = []
    while True:
        commands.append(input("> "))
        if commands[-1] == "q":
            commands.pop()
            break

    while True:
        time_now = time.strftime("%H:%M", time.localtime(time.time()))
        if time_now == t:
            for command in commands:
                os.system(command)
                time.sleep(3)
            print("All commands is done!")
            break
        time.sleep(30)

if __name__ == "__main__":
    pusher()
