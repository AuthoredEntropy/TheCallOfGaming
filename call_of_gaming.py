#Author: @AuthoredEntropy 
import tkinter as tk
import time
import threading
import tkinter.font as tkFont
author = "@AuthoredEntropy"
window = tk.Tk()
window.geometry("400x75")
window.title("")
window.config(bg="#a8a8a8")
def addVerticalSpacer(master, h,  color ="#a8a8a8"):
    spacer = tk.LabelFrame(master=master, height=h, bg =color,relief="flat")
    spacer.pack(fill="both")
    return spacer
def addHorizontalSpacer(master, w, color ="#a8a8a8"):
    spacer = tk.LabelFrame(master=master, width=w, bg =color, relief="flat")
    spacer.pack(side=tk.LEFT, fill="both")
def denounceFunc(main,top):
    main.pack_forget()
    youHaveDenounced = tk.Label(top, text="you have denounced gaming...\n goobye")
    youHaveDenounced.place(relx=0.5, rely=0.5,anchor="center")
def callLoadLoop(label):
    while("calling" in label["text"]):
        if("..." in label["text"]):
            label.config(text="calling gaming.")
        else:
            label.config(text=label["text"] + ".")
        time.sleep(1)
    return
def waitThenStop(label, msg):
    time.sleep(10)
    label.config(text=msg)
def callFunc(main,top,msg):
    main.pack_forget()
    fontStyle = tkFont.Font(family="Lucida Grande", size=20)
    youHaveCalled = tk.Label(top, text="calling gaming.", font=fontStyle)
    youHaveCalled.place(relx=0.5, rely=0.5,anchor="center")
    x = threading.Thread(target=callLoadLoop, args=(youHaveCalled,))
    x.start()
    y = threading.Thread(target=waitThenStop, args=(youHaveCalled,msg,))
    y.start()

def yesFunc():
    top = tk.Toplevel()
    top.geometry("400x350")
def noFunc():
    top = tk.Toplevel()
    top.geometry("400x350")
    main =tk.Frame(top, width=350,height=400)
    main.pack_propagate(0)
    main.pack()
    addVerticalSpacer(main,100, top["bg"])
    middle = addVerticalSpacer(main,50, top["bg"])
    denounceGaming = tk.Label(middle, text="denounce gaming, or call it, the choice is yours")
    denounceGaming.place(relx=0.5, rely=0.5,anchor="center")
    lower = addVerticalSpacer(main,25, top["bg"])
    call = tk.Button(master=lower, text="call", height=3, width=9,command = lambda: callFunc(main,top,"gaming has answered your call"))
    denounce = tk.Button(master=lower, text="denounce", height=3, width=9,command = lambda: denounceFunc(main,top))
    addHorizontalSpacer(lower,95,top["bg"])
    denounce.pack(side="left" ,anchor="center")
    addHorizontalSpacer(lower,15,top["bg"])
    call.pack(side="left",anchor="center")
def expandWindow(window, w,h,button,hideButton, label, willYouAnswer):
    if(label["text"] == "you have ignored gaming..."):
        window.geometry(f"{w}x{h}")
        button.pack_forget()
        willYouAnswerText.config(text="gaming will not call again")
        button = tk.Button(window, text ="read more", relief="flat", bg="#a8a8a8" ,activebackground="#a8a8a8", activeforeground="blue")
        button.pack(side="bottom", anchor="s")
        def secondExpand():
            willYouCallGaming = tk.Frame(master=window, width=400,height=125, bg="#757575")
            willYouCallGaming.pack()
            window.geometry(f"400x325")
            button.pack_forget()
            willYouAnswerText.config(text="but will you call it?")
            yes = tk.Button(master=willYouCallGaming, text = "yes", height=2, width=5,command=yesFunc)
            no = tk.Button(master=willYouCallGaming, text = "no", height=2, width=5, command=noFunc)
            addVerticalSpacer(window, 25)
            yes.pack(side="left", anchor="center")
            addHorizontalSpacer(willYouCallGaming, 5)
            no.pack(side="left", anchor="center")
        button.config(command=secondExpand)
        return
    button.pack_forget()
    hideButton.pack(side="bottom", anchor="s")
    window.geometry(f"{w}x{h}")
def hideWindow(window,w,h,hideButton, button, label):
    label.config(text="you have ignored gaming...")
    hideButton.pack_forget()
    button.pack()
    window.geometry(f"{w}x{h}")
gamingIsCallingFrame = tk.Frame(master=window, width=400,height=50)
gamingIsCallingFrame.pack()
gamingIsCallingFrame.pack_propagate(0)
gamingIsCallingText = tk.Label(master=gamingIsCallingFrame, text="Gaming is calling...")
gamingIsCallingText.place(relx=0.5, rely=0.5,anchor="center")
readMore = addVerticalSpacer(window, 25, "#a8a8a8") 
button = tk.Button(readMore, text ="read more", relief="flat", bg="#a8a8a8" ,activebackground="#a8a8a8", activeforeground="blue")
button.pack()
willYouAnswerFrame = tk.Frame(master=window, width=400, height=100, bg="#a8a8a8")
willYouAnswerFrame.pack()
willYouAnswerText = tk.Label(willYouAnswerFrame, text="Will you answer?", bg="#a8a8a8")
willYouAnswerText.place(relx=0.5, rely=0.5,anchor="center")
spacer2 = addVerticalSpacer(window, 25, "#a8a8a8") 
hide = tk.Button(window, text ="hide", relief="flat", bg="#a8a8a8" ,activebackground="#a8a8a8", activeforeground="blue")
hide.config(command= lambda: hideWindow(window, 400,75, hide, button, gamingIsCallingText))
button.config(command=lambda: expandWindow(window,400,225,button, hide, gamingIsCallingText, willYouAnswerText))
hide.pack(side="bottom", anchor="s")
window.mainloop()