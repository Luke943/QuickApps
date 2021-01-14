import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

# initialise
root = tk.Tk()
root.title("PDF Text Extractor")

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# theme
style = ThemedStyle(root)
style.set_theme("scidpink")

# logo
logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = ttk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions
instructions = ttk.Label(root, text="Select a PDF file to extract its text")
instructions.grid(columnspan=3, column=0, row=1)


def open_file():
    browse_text.set("Loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file",
                       filetype=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        # text box
        text_box = tk.Text(root)
        text_box.insert(1.0, page_content)
        text_box.grid(column=1, row=3)

    browse_text.set("Browse")


def on_closing():
    # function for closing event
    root.destroy()


# browse button
browse_text = tk.StringVar()
browse_text.set("Browse")
browse_btn = ttk.Button(root, textvariable=browse_text, command=lambda: open_file())
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

# on close window
root.protocol("WM_DELETE_WINDOW", on_closing)

# close main program
root.mainloop()
