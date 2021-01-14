import tkinter as tk
from PIL import Image, ImageTk
from functions import *

glossary_file = "glossary.txt"
add_msg = "Add to glossary"
edit_msg = "Save changes"


def on_search():
    entered_text = text_entry.get()
    output.delete(0.0, "end")
    try:
        definition = my_dictionary[entered_text.lower()]
        add_edit_text.set(edit_msg)
    except:
        definition = "Sorry, that word is not in the glossary.\nSearch again or enter a definition here and click below to save."
        add_edit_text.set(add_msg)
    output.insert("end", definition)
    add_button.grid(row=6, column=0)


def on_change():
    key = text_entry.get().lower()
    value = output.get(1.0, "end")
    if add_edit_text.get() == edit_msg:
        edit_glossary(key, value, glossary_file)
    elif add_edit_text.get() == add_msg:
        add_glossary(key, value, glossary_file)
    my_dictionary[key] = value


# initialise dictionary from file
my_dictionary = create_dictionary(glossary_file)

# initialise Tk class
app = tk.Tk()
app.title("My Glossary")
app.configure(bg="gray")
canvas = tk.Canvas(app, width=400, height=400)

# logo
logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=0, row=0)

# label for instruction
instruction_label = tk.Label(app, text="Enter the word you would like a definition for:",
                             bg="gray", fg="#ffcd0e", font="none 12 bold", padx=15, pady=15)
instruction_label.grid(column=0, row=1)

# text entry box
text_entry = tk.Entry(app, width=20, bg="white", font="none 12")
text_entry.grid(row=2, column=0)

# search button
search_button = tk.Button(
    app, text="Search", font="none 12", width=6, command=on_search)
search_button.grid(row=3, column=0)

# label for definition
instruction_label = tk.Label(app, text="Definition:",
                             bg="gray", fg="#ffcd0e", font="none 12 bold", padx=15, pady=15)
instruction_label.grid(column=0, row=4)

# output box
output = tk.Text(app, width=42, height=6, bg="white", font="none 12")
output.grid(row=5, column=0)

# add/edit button
add_edit_text = tk.StringVar()
add_button = tk.Button(
    app, textvariable=add_edit_text, font="none 12", command=on_change)

app.mainloop()
