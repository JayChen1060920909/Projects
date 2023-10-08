import PyPDF2, pyttsx3

path = open("C - Operators.pdf",'rb')

pdfReader = PyPDF2.PdfFileReader(path)

speak = pyttsx3.init()

for page in range(pdfReader.numPages):
    text = pdfReader.getPage(page).extractText()
    speak.say(text)
    speak.runAndWait()
speak.stop()

