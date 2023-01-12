import time
import tkinter as tk
import http.client
postBackward = http192.168.10.228postBackward
postForward = http192.168.10.228postForward
postTurnLeft =http192.168.10.228postTurnLeft
postTurnRight = http192.168.10.228postTurnRight
h1 = http.client.HTTPConnection('192.168.10.228')


class Example(tk.Frame)
    def __init__(self, parent)
        tk.Frame.__init__(self, parent, width=400,  height=400)

        self.label = tk.Label(self, text=last key pressed  , width=20)
        self.label.pack(fill=both, padx=100, pady=100)

        self.label.bind(w, self.on_wasd)
        self.label.bind(a, self.on_wasd)
        self.label.bind(s, self.on_wasd)
        self.label.bind(d, self.on_wasd)

        # give keyboard focus to the label by default, and whenever
        # the user clicks on it
        self.label.focus_set()
        self.label.bind(1, lambda event self.label.focus_set())

    def on_wasd(self, event)
        self.label.configure(text=last key pressed  + event.keysym);
        if event.keysym == w
            print(w)
            h1.request('POST', 'postForward')
            h1.close()

        elif event.keysym == a
            print(a)
            h1.request('POST', 'postTurnLeft')
            h1.close()
        elif event.keysym == s
            print(s)
            h1.request('POST', 'postBackward')
            h1.close()
        elif event.keysym == d
            print(d)
            h1.request('POST', 'postTurnRight')
            h1.close()


if __name__ == __main__
    #while True
    #    h1.request('POST', 'postForward')
    #    h1.close()
    #    time.sleep(1.1)
    #    h1.request('POST', 'postTurnRight')
    #    h1.close()
    #    time.sleep(1.1)
    root = tk.Tk()
    Example(root).pack(fill=both, expand=True)
    root.mainloop()