import fitz
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import typing
from borb.pdf.document.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction
import os
import json
def access_file():

        dir_path = r'static/pdf'
        res=[]
        for path in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                res.append(path)
        return  res
# ---------------replicating given pdf to avoid errors occurring by  verifying image pdf!-----------------
'''def replicating(res):
    reader = PdfReader('static/pdf/'+str(res[0]),strict=False)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    with open("main_pdf_file/fixedPDF.pdf", "wb") as fp:
        writer.write(fp)
        merger = PdfMerger()
    merger.append("main_pdf_file/fixedPDF.pdf")'''

#---------------------------- font detection!-

def scrape(filePath):
    results = []     # list of tuples that store the information as (text, font size, font name)
    pdf = fitz.open(filePath)         # filePath is a string that contains the path to the pdf
    for page in pdf:
        dicts = page.get_text("dict")
        blocks = dicts["blocks"]
        for block in blocks:
            if "lines" in block.keys():
                spans = block['lines']
                for span in spans:
                    data = span['spans']
                    for lines in data:
                               results.append((lines['text'], lines['size'], lines['font']))
                            # lines['text'] -> string, lines['size'] -> font size, lines['font'] -> font name
    pdf.close()
    return results

 #  ------------------------------ checking for mismatch font syle--------------------------
def mismatch_font_style(path):

    li=scrape(path)
    li2=[]
    for l in li:
        a= (l[2].split('-')[0])
        if str(a) not in "'ClassGarmnd','ClassGarmndBT','ClassicalGaramondBT', 'FrutigerLTPro', 'FrutigerLTStd', 'Symbol', 'TimesNewRoman', 'Arial','ArialMT','ArialNarrow":
             li2.append(l[2])
    if li2:
       return False
    else:
        return True

#---------------------------------minimum lines-----------------------------------------

def min_lines(path):
    global ans
    page_lines = {}
    itr = 0
    # read the Document
    doc: typing.Optional[Document] = None
    l: SimpleTextExtraction = SimpleTextExtraction()
    with open(path, "rb") as in_file_handles:
       doc = PDF.loads(in_file_handles, [l])

    # check whether we have read a Document
    assert doc is not None

    # print the text on the first Page

    pg = int(doc.get_document_info().get_number_of_pages())
    for a in range(pg):
        count = 0
        b = l.get_text_for_page(a)

        for i in b.split('\n'):

            count = count + 1
            page_lines[a] = count

    for p in page_lines.values():

        if p < 5:

            ans= False
        else:
            ans= True

    return ans

def check(res):
        min_lines_out=min_lines('static/pdf/'+str(res[0]))
        mismatch_font_style_out=mismatch_font_style('static/pdf/'+str(res[0]))
        if(min_lines('static/pdf/'+str(res[0]))) and (mismatch_font_style('static/pdf/'+str(res[0]))):
            validity="pdf correct"
            return validity,mismatch_font_style_out,min_lines_out
        else:
            validity="error"
            return validity,mismatch_font_style_out,min_lines_out

def json_write(validity,mismatch_font_style_out,min_lines_out):

    dictionary ={
        "pdf_validity": validity,
        "correct_font_style": mismatch_font_style_out,
        "number_of_lines>5":min_lines_out,
        "Missing_header_or_footer":"under_construction",
        "Short_column":"under_construction",
        "Text_exceeds_margin": "under_construction",
        "Missing_Entity":"under_construction"

    }

    with open("static/sample.json", "w") as outfile:
        json.dump(dictionary, outfile)
# Python program to explain os.remove() method

# importing os module

def delete_File(res):
    # File name
    file = res[0]

    # File location
    dir = "static/pdf"

    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    # Remove the file
    # 'file.txt'