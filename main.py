import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger
from PIL import Image, ImageTk

# Ahora almacenaremos los nombres de archivo en estas variables
file1 = None
file2 = None

root = tk.Tk()
root.title("PDF Merger")
root.geometry("250x310") #Dimensiones
root.iconbitmap('pdf.ico')
root.configure(bg="#FFABAB")

# Disable window resizing
root.resizable(False, False)

# Crea un frame para contener los elementos
frame = tk.Frame(root, bg="#FFABAB")
frame.pack(expand=True, fill="both", padx=20, pady=20)

# Load the image
image = Image.open("photo.png")
image = image.resize((100, 100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

def browse_file_1():
    global file1  # Usa la variable global file1
    file1 = filedialog.askopenfilename(filetypes=(("PDF files", "*.pdf"),("All files", "*.*")))
    label1.config(text="File 1: " + file1 + ".pdf")

def browse_file_2():
    global file2  # Usa la variable global file2
    file2 = filedialog.askopenfilename(filetypes=(("PDF files", "*.pdf"),("All files", "*.*")))
    label2.config(text="File 1: " + file2 + ".pdf")

def merge_pdfs():
    if file1 is None or file2 is None:  # Si no se seleccionaron archivos, no hagas nada
        return

    pdf_merger = PdfMerger()
    files = [file1, file2]

    for file in files:
        pdf_merger.append(file)

    output = filedialog.asksaveasfilename(defaultextension=".pdf")
    pdf_merger.write(output)
    pdf_merger.close()

button1 = tk.Button(frame, text="Select 1st PDF", command=browse_file_1)
button1.pack(pady=5)  # Espaciado vertical

# Crea etiquetas de texto
label1 = tk.Label(frame, text="Not Selected", bg="#FFABAB")
label1.pack()

button2 = tk.Button(frame, text="Select 2nd PDF", command=browse_file_2)
button2.pack(pady=5)  # Espaciado vertical

label2 = tk.Label(frame, text="Not Selected", bg="#FFABAB")
label2.pack()

# Crea una etiqueta con la imagen
labelPhoto = tk.Label(frame, image=photo, bg="#FFABAB")
labelPhoto.pack(pady=10)  # Espaciado vertical

button3 = tk.Button(frame, text="Merge PDFs", command=merge_pdfs)
button3.pack(pady=5)  # Espaciado vertical

root.mainloop()