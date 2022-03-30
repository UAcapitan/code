import peewee
import json
import names
import random
import tkinter as tk

data_for_generation = {
    'email_hosts': 
        ['gmail', 'email', 'text', 'uamail', 'example', 'newmail', 'mail'],
    'domains': 
        ['ua', 'ge', 'us', 'fr', 'com', 'net', 'org']
}

class App:
    def __init__(self):
        self.root = tk.Tk()

if __name__ == '__main__':
    print('Start working') #TODO delete
    app = App()

