from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import os
import time
import psutil
from tkinter import messagebox
import zipfile
import tkinter.font as tkFont

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x =(screen_width - width) // 2
    y =(screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def run():
    mem_byte = psutil.virtual_memory().total
    mem_gib = str(int(mem_byte / (1024.**2)))
    cpu_count = str(int(os.cpu_count()))
    try:
        if (os.path.isfile("utils\\arch.IMG") == True):
            root.destroy()
            os.system('utils\\lfw-core -m '+ mem_gib +' -smp '+ cpu_count +' -nographic -hda utils\\arch.IMG -accel whpx -name "LFW" -bios utils\\bios.bin')
            
        else:
            if(os.path.isfile("utils\\arch.rom") == True):
                with zipfile.ZipFile("utils\\arch.rom", 'r') as zip_ref:
                    zip_ref.extractall("utils\\")
                    os.remove("utils\\arch.rom")
                    root.destroy()
                    os.system('utils\\lfw-core -m '+ mem_gib +' -smp '+ cpu_count +' -nographic -hda utils\\arch.IMG -accel whpx -name "LFW" -bios utils\\bios.bin')
                    
            else:
                msg = messagebox.showerror("Error", "Rom File Not Found")
                root.destroy()
    except:
        msg = messagebox.showerror("Error", "SomeThing Wrong Happened!!")
        root.destroy()
    


root = tk.Tk()
center_window(root, 500, 100)
font1 = tkFont.Font(family="Helvetica", size=26)
root.title('LFW')
root.iconbitmap("icon.ico")
root.resizable(0,0)
root.overrideredirect(True)
root.configure(bg = "#111111")
image1 = Image.open("icon.png")
img = image1.resize((75, 75))  
test = ImageTk.PhotoImage(img)
label1 = Label(image=test,bg="#111111")
label1.image = test
# Position image
label1.place(x="20px",y="6px")

Label(text="Linux for Windows", font=font1, fg="white", bg="#111111").place(x="110px", y="20px")
root.after(5000,run)
root.mainloop()




