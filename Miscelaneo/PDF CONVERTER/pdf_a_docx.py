from PyPDF2 import PdfFileReader, PdfFileWriter
from pdf2docx import Converter
import os

def unlock_pdf(input_pdf, output_pdf, password):
    with open(input_pdf, 'rb') as infile:
        reader = PdfFileReader(infile)
        if reader.isEncrypted:
            reader.decrypt(password)
            writer = PdfFileWriter()
            for page_num in range(reader.numPages):
                writer.addPage(reader.getPage(page_num))
            with open(output_pdf, 'wb') as outfile:
                writer.write(outfile)
            print(f"Desbloqueo del PDF completado: {output_pdf}")
        else:
            print("El PDF no está protegido por contraseña.")

def convert_pdf_to_word(input_pdf, output_docx):
    cv = Converter(input_pdf)
    cv.convert(output_docx, start=0, end=None)
    cv.close()
    print(f"Conversión a Word completada: {output_docx}")

# Rutas de archivo
input_pdf = "ruta/al/archivo/protegido.pdf"
unlocked_pdf = "ruta/al/archivo/desbloqueado.pdf"
output_docx = "ruta/al/archivo/convertido.docx"
password = "tu_contraseña"

# Desbloquear el PDF
unlock_pdf(input_pdf, unlocked_pdf, password)

# Convertir el PDF desbloqueado a Word
convert_pdf_to_word(unlocked_pdf, output_docx)

# Limpiar el archivo PDF desbloqueado si ya no es necesario
os.remove(unlocked_pdf)