import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pyttsx3
from PyPDF2 import PdfReader

engine = pyttsx3.init()

def speak_text(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def speak_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("PDF Files", "*.pdf")])
    if file_path:
        try:
            if file_path.endswith(".txt"):
                with open(file_path, 'r') as file:
                    text = file.read()
                    speak_text(text)
            elif file_path.endswith(".pdf"):
                pdf_text = extract_text_from_pdf(file_path)
                speak_text(pdf_text)
        except Exception as e:
            print(f"Error reading or speaking the file: {e}")

def extract_text_from_pdf(pdf_file):
    pdf_text = ""
    try:
        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:
            pdf_text += page.extract_text()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
    return pdf_text

root = Tk()
root.title("Text to Speech from File")
root.geometry("400x200")
root.resizable(False, False)

obj = LabelFrame(root, text="Text to speech", font=20, bd=1)
obj.pack(fill="both", expand="yes", padx=10, pady=10)

btn_open_file = Button(obj, text="Open File", font=20, bg="black", fg="white", command=speak_file)
btn_open_file.pack(side=tk.LEFT, padx=10)

root.mainloop()
