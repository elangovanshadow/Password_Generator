import tkinter
import pandas
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_entry.delete(0,'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list = password_list + [random.choice(letters) for x in range(nr_letters) ]
    password_list = password_list + [random.choice(symbols) for x in range(nr_symbols) ]
    password_list = password_list + [random.choice(numbers) for x in range(nr_numbers) ]


    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# heading = ['Website','mailID','Password']
# df = pandas.DataFrame(columns=heading)
# df.to_csv('data.csv',header=True)
def save():
    if len(website_entry.get()) == 0 or len(mailID_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror(title="Empty Error",message='Please don\'t leave any fields empty' )
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f'Your Entries are\nEmail : {mailID_entry.get()}\nPassword : {password_entry.get()}\nis it ok to continue')
        if is_ok:
            data = [website_entry.get(),mailID_entry.get(),password_entry.get()]
            data_csv = pandas.DataFrame(columns=data)
            data_csv.to_csv('data.csv',mode='a')
            website_entry.delete(0,'end')
            password_entry.delete(0,'end')
            website_entry.focus()
    # ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=100,pady=100)

image = tkinter.PhotoImage(file='logo.png')
canvas = tkinter.Canvas(width=200,height=200)
canvas.create_image(100,100,image=image)
canvas.grid(row=1,column=2)


website_label = tkinter.Label(text='Website:')
website_label.grid(row=2,column=1)

website_entry = tkinter.Entry(width=52)
website_entry.grid(row=2,column=2,columnspan=2)
website_entry.focus()

mailID_label = tkinter.Label(text='Email/Username:')
mailID_label.grid(row=3,column=1)

mailID_entry = tkinter.Entry(width=52)
mailID_entry.grid(row=3,column=2,columnspan=2)
mailID_entry.insert(0,'elango958533675@gmail.com')

password_label = tkinter.Label(text='Password:')
password_label.grid(row=4,column=1)

password_entry = tkinter.Entry(width=33)
password_entry.grid(row=4,column=2,columnspan=1)

add_button = tkinter.Button(text='Add',width=44,command=save)
add_button.grid(row=5,column=2,columnspan=2)


password_generate_button = tkinter.Button(text='Generate Password',command=password_generator)
password_generate_button.grid(row=4,column=3)










window.mainloop()