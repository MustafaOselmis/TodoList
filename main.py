import tkinter
from PIL import Image,ImageTk
from tkinter import messagebox

#screen

def Saving():
    title = entry1.get()
    message = textbox1.get("1.0", "end-1c")
    if len(title) == 0 or len(message) == 0 :
        messagebox.showerror(title="Error",message="Please enter all info")
    else:
        try:
           with open("todolist.txt","a") as datafile:
               datafile.write(f'\n{title}\n{message}\n')
        except FileNotFoundError:
            with open("mysecret.txt","w") as datafile:
                datafile.write(f'\n{title}\n{message}')
        finally:
            entry1.delete("0","end")    
            textbox1.delete("1.0","end")
            
    

window = tkinter.Tk()
window.title("Secret Notes")
window.config(padx=20,pady=20,bg="grey")
window.minsize(width=400,height=800)
fontX= ("Arial","18")

# Upload the image

img = Image.open(r"C:\Users\must\Desktop\python_temelleri\To do List\foto.png")
img = img.resize((200, 200))
photo = ImageTk.PhotoImage(img)

# Show the image
label1 = tkinter.Label(window, image=photo,bg="grey")
label1.pack()

# Title label

label2 = tkinter.Label(text="Enter Your Title",bg="grey", fg="black",padx=20,pady=10,font=fontX)
label2.pack()

#entry 1

entry1 = tkinter.Entry(width=20)
entry1.pack()

# Enter the program

label3= tkinter.Label(text="Schedule",bg="grey", fg="black",padx=20,pady=20,font=fontX)
label3.pack()

# textbox

textbox1 = tkinter.Text(window,height=15,width=25)
textbox1.pack(pady=(0, 25))


# button 1 = Save / Encrpyt

button1 = tkinter.Button()
button1.config(text="Save ",width=15,height=3,command=Saving)
button1.pack(pady=5)

window.mainloop()