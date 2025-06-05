import pyttsx3
import PyPDF2 as pdf
from tkinter.filedialog import askopenfilename
from tkinter import Tk


Tk().withdraw()

book = askopenfilename()

pdfreader = pdf.PdfReader(book)
num_of_pages = len(pdfreader.pages)

player = pyttsx3.init()

for num in range(num_of_pages):
    page = pdfreader.pages[num]          
    text = page.extract_text()           
    if text:                             
        player.say(text)

player.runAndWait()

