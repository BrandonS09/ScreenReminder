import customtkinter
import sys
import CTkMessagebox
import time as TimeModule
# This bit gets the taskbar icon working properly in Windows
if sys.platform.startswith('win'):
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'CompanyName.ProductName.SubProduct.VersionInformation') # Arbitrary string
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.title("Screen Reminder")
root.geometry("520x280")
root.iconbitmap(default="icon.ico")
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both")
root.resizable(False, False)
label = customtkinter.CTkLabel(master=frame, text="Screen Reminder", font=("Roboto Bold", 50))
label.pack(pady=12, padx=10)

def combobox_called(choice):
    print(choice)
    Alarm(choice=choice)

timeLabel = customtkinter.CTkLabel(master=frame, text="Remind me to look away every: ", font=("Open Sans", 16))
time = customtkinter.CTkComboBox(master=frame, values=["Never", "10 min", "15 min","20 min", "30 min", "45 min", "1 hour"], command=combobox_called, state="readonly")
timeLabel.pack(pady=48, padx=10, side="left")
time.pack(pady=48, padx=10, side="left")
time.set("None")
def CheckDestroyed(box):
    if CTkMessagebox.CTkMessagebox.Isdestroyed(box):
        return True
    
def tenmin():
    box = CTkMessagebox.CTkMessagebox(title="Screen Alarm", message=str("Its been 10 minutes! Time to get up and move around!"), option_1="OK")
    def Check():
        if CheckDestroyed(box):
            Alarm("10 min")
            print("Passed")
        else:
            root.after(1000,Check)
            print("Checking")
    Check()

def fifteenmin():
    box = CTkMessagebox.CTkMessagebox(title="Screen Alarm", message=str("Its been 15 minutes! Time to get up and move around!"), option_1="OK")
    def Check():
        if CheckDestroyed(box):
            Alarm("15 min")
            print("Passed")
        else:
            root.after(1000,Check)
            print("Checking")
    Check()

def twentymin():
    box = CTkMessagebox.CTkMessagebox(title="Screen Alarm", message=str("Its been 20 minutes! Time to get up and move around!"), option_1="OK")
    def Check():
        if CheckDestroyed(box):
            Alarm("20 min")
            print("Passed")
        else:
            root.after(1000,Check)
            print("Checking")
    Check()

def thirtymin():
    box = CTkMessagebox.CTkMessagebox(title="Screen Alarm", message=str("Its been 30 minutes! Time to get up and move around!"), option_1="OK")
    def Check():
        if CheckDestroyed(box):
            Alarm("30 min")
            print("Passed")
        else:
            root.after(1000,Check)
            print("Checking")
    Check()

def fourtyfivemin():
    box = CTkMessagebox.CTkMessagebox(title="Screen Alarm", message=str("Its been 45 minutes! Time to get up and move around!"), option_1="OK")
    def Check():
        if CheckDestroyed(box):
            Alarm("45 min")
            print("Passed")
        else:
            root.after(1000,Check)
            print("Checking")
    Check()

def hour():
    box = CTkMessagebox.CTkMessagebox(title="Screen Alarm", message=str("Its been 1 hour! Time to get up and move around!"), option_1="OK")
    def Check():
        if CheckDestroyed(box):
            Alarm("1 hour")
            print("Passed")
        else:
            root.after(1000,Check)
            print("Checking")
    Check()

def Alarm(choice):
    print(choice)
    if choice != "None":
        if choice == "10 min":
            root.after(10 * 60000, tenmin)
        elif choice == "15 min":
            root.after(15 * 60000, fifteenmin)       
        elif choice == "20 min":
            root.after(20*60000, twentymin)
        elif choice == "30 min":
            root.after(30*60000,thirtymin)
        elif choice=="45 min":
            root.after(45*60000,fourtyfivemin)
        elif choice == "1 hour":
            root.after(60*60000, hour)
            
root.mainloop()