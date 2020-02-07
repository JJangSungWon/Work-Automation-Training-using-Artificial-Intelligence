#hwp
import os
import pandas as pd

import olefile

#pdf
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

#hwp
f = olefile.OleFileIO('test.hwp')
encoded_text = f.openstream('PrvText').read()
decoded_text = encoded_text.decode('UTF-16') #유니코드이므로 utf-15으로 디코딩한다.
print(decoded_text)


#pdf
def pdf2txt():
    rsrcmgr = PDFResourceManager()

    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open('test.pdf', 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

v = pdf2txt()
print(v)
