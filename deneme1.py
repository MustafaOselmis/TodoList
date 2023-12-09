import tkinter
from PIL import Image, ImageTk

#screen
window = tkinter.Tk()
window.title("Secret Notes")
window.config(padx=20, pady=20, bg="grey")
window.minsize(width=400, height=800)
fontX = ("Arial", "18")

# Upload the image
img = Image.open(r"C:\Users\must\Desktop\python_temelleri\To do List\foto.png")
img = img.resize((200, 200))
photo = ImageTk.PhotoImage(img)

# Show the image
label1 = tkinter.Label(window, image=photo, bg="grey")
label1.pack()

# Title label
label2 = tkinter.Label(text="Enter Your Title", bg="grey", fg="black", padx=20, pady=10, font=fontX)
label2.pack()

# entry 1
entry1 = tkinter.Entry(width=20)
entry1.pack()

# Enter the program
label3 = tkinter.Label(text="Schedule", bg="grey", fg="black", padx=20, pady=20, font=fontX)
label3.pack()

# textbox
textbox1 = tkinter.Text(window, height=15, width=25)
textbox1.pack(pady=(0, 10))  # Yüksekliği sıfıra ayarlayarak bir boşluk bırakıyoruz.

# button 1 = Save / Encrypt
button1 = tkinter.Button(text="Save", width=15, height=3)
button1.pack(pady=5)

window.mainloop()