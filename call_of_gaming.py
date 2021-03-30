#Author: @AuthoredEntropy 
import tkinter as tk
import time
import threading
import tkinter.font as tkFont
import random
author = "@AuthoredEntropy"
window = tk.Tk()
window.geometry("400x75")
window.iconbitmap(default='transparent.ico')
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
    youHaveDenounced = tk.Label(top, text="you have denounced gaming... \n May God have mercy")
    youHaveDenounced.place(relx=0.5, rely=0.3,anchor="center")
    fontStyle = tkFont.Font(family="Lucida Grande", size=20)
    timerLabel = tk.Label(top, text="Gaming will find you in:")
    timerLabel.place(relx=0.5, rely=0.4,anchor="center")
    timer = tk.Label(top, text="10", font=fontStyle)
    timer.place(relx=0.5, rely=0.5,anchor="center")
    x = threading.Thread(target=waitThenClose, args=(10,timer,timerLabel,youHaveDenounced,top,))
    x.start()
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
def checkInt(num):
    try:
        int(num)
    except:
        return False
    return True
def funnyText(timer,top):
    fontStyle = tkFont.Font(family="Lucida Grande", size=50)
    timer.config(foreground="red", bg="black", font=fontStyle)
    top.config(bg="black")
    top.attributes("-fullscreen", True)
    num = 0
    while("gaming" in timer["text"]):
        rand1 = random.uniform(-0.1, 0.1)
        rand2 = random.uniform(-0.1, 0.1)
        if(num%25 ==0):
            rand1 = random.uniform(-0.3, 0.3)
            rand2 = random.uniform(-0.3, 0.3)
        timer.place_forget() 
        timer.place(relx=0.5+rand1, rely=0.4+rand2,anchor="center")
        time.sleep(.01)
        num +=1
        if(num > 500):
            
            timer.config(text="death")
            time.sleep(.1)
            top.attributes("-fullscreen", False)
    y = threading.Thread(target=funnyText2, args=(timer,0.01,.4,.5,.1,))
    y.start()
    fontStyle2 = tkFont.Font(family="Lucida Grande", size=25)
    smallerText = tk.Label(top, text="death", font=fontStyle2, foreground="red",bg="black")
    smallerText.place(relx=0.2+rand1, rely=0.3+rand2,anchor="center")
    smallerTextThread = threading.Thread(target=funnyText2, args=(smallerText,0.01,.2,.3,.1,))
    smallerTextThread.start()
    smallerText2 = tk.Label(top, text="death", font=fontStyle2, foreground="red",bg="black")
    smallerText2.place(relx=0.2+rand1, rely=0.3+rand2,anchor="center")
    smallerText3 = tk.Label(top, text="death", font=fontStyle2, foreground="red",bg="black")
    smallerText3.place(relx=0.2+rand1, rely=0.3+rand2,anchor="center")
    smallerTextThread2 = threading.Thread(target=funnyText2, args=(smallerText2,0.01,.6,.8,.1,))
    smallerTextThread2.start()
    smallerTextThread3 = threading.Thread(target=funnyText2, args=(smallerText3,0.01,.4,.8,.3,))
    smallerTextThread3.start()
    smallerText4 = tk.Label(top, text="death", font=fontStyle2, foreground="red",bg="black")
    smallerText4.place(relx=0.2+rand1, rely=0.3+rand2,anchor="center")
    smallerTextThread5 = threading.Thread(target=funnyText2, args=(smallerText4,0.01,.1,.8,.3, ))
    smallerTextThread5.start()
    time.sleep(10)
    smallerText3.config(text="dead")
    smallerText4.config(text="dead")
    smallerText.config(text="dead")
    smallerText2.config(text="dead")
    timer.config(text="dead")
    time.sleep(.1)
    window.quit()
def funnyText2(text,delay, startY,startX,mod):
    num = 0
    txtName = text["text"]
    while(text["text"] ==txtName): 
        rand1 = random.uniform(-mod, mod)
        rand2 = random.uniform(-mod, mod)
        if(num%25 ==0):
            rand1 = random.uniform(-(mod*3), mod*3)
            rand2 = random.uniform(-(mod*3), mod*3)
        text.place_forget() 
        text.place(relx=startX+rand1, rely=startY+rand2,anchor="center")
        time.sleep(delay)
        num +=1
    return
def stopWatch(timer,hide1,hide2,top):
    while(int(timer["text"]) > 1):
        timer.config(text=int(timer["text"])-1) 
        time.sleep(1)
    timer.place_forget() 
    hide1.place_forget() 
    hide2.place_forget() 
    timer.place(relx=0.5, rely=0.4,anchor="center")
    timer.config(text="gaming has found you")
    y = threading.Thread(target=funnyText, args=(timer,top,))
    y.start()
def waitThenClose(t, timer, hide1,hide2,top):
    timer.config(text=str(t))
    if(checkInt(timer["text"])):
        x = threading.Thread(target=stopWatch, args=(timer,hide1,hide2,top,))
        x.start()
def yesFunc():
    top = tk.Toplevel()
    top.geometry("400x350")
    main =tk.Frame(top, width=350,height=400)
    callFunc(main,top,"gaming has answered your call")
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