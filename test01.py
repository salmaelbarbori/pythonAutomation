import pyttsx3
import PyPDF3

pdf_file = open(r"path", 'rb')
# rb meaning : reading the file in binary mode
reader = PyPDF3.PdfFileReader(pdf_file, strict=False)
number_of_pages = reader.getNumPages()
engine = pyttsx3.init()
for i in range(0, 1):
    page = reader.getPage(i)
    page_content = page.extractText()
    # specify the volume
    newrate = 200
    engine.setProperty('rate', newrate)
    newvolume = 200
    engine.setProperty('volume', newvolume)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.save_to_file(page_content, 'pdf_audio.mp3')
    engine.runAndWait()
    engine.stop()
