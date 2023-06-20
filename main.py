import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger

# Ahora almacenaremos los nombres de archivo en estas variables
file1 = None
file2 = None

root = tk.Tk()
root.title("PDF Merger")
root.geometry("250x100") #Dimensiones
root.iconbitmap('pdf.ico')
root.configure(bg="#ff1f48")
label1 = tk.Label(root, text="Not Selected",bg="#ff1f48")
label2 = tk.Label(root, text="Not Selected",bg="#ff1f48")
label1.grid(row=0, column=1)
label2.grid(row=1, column=1)

def browse_file_1():
    global file1  # Usa la variable global file1
    file1 = filedialog.askopenfilename(filetypes=(("PDF files", "*.pdf"),("All files", "*.*")))
    label1.setvar("File 1: " + file1 + ".pdf")

def browse_file_2():
    global file2  # Usa la variable global file2
    file2 = filedialog.askopenfilename(filetypes=(("PDF files", "*.pdf"),("All files", "*.*")))
    label2.setvar("File 1: " + file2 + ".pdf")

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

canvas = tk.Canvas(root, width=200, height=200, bd=0, highlightthickness=0)
canvas.pack()

button1 = tk.Button(root, text="Seleccionar PDF 1", command=browse_file_1)
button1.grid(row=0, column=0)  # Posiciona en la primera fila, primera columna

button2 = tk.Button(root, text="Seleccionar PDF 2", command=browse_file_2)
button2.grid(row=1, column=0)  # Posiciona en la segunda fila, primera columna

button3 = tk.Button(root, text="Unir PDFs", command=merge_pdfs)
button3.grid(row=2, column=0)  # Posiciona en la tercera fila, primera columna

root.mainloop()
