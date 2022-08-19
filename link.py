from flask import Flask,render_template,request,redirect, url_for
import os
from main import  *
app = Flask(__name__,
 template_folder="temp",
    static_folder="static")


def long_load(typeback):
   time.sleep(5)  # just simulating the waiting period
   return "You typed: %s" % typeback

from werkzeug.utils import secure_filename
app.config['PDF_uploads']='/Users/sange/Desktop/kiriyadocs- codeathon/static/pdf'

@app.route('/',methods=['GET','POST'])
def main_page():
   return render_template("index.html")

@app.route('/pdf_processing',methods=['POST'])
def get_pdf():
   if request.method == 'POST':
      pdf=request.files['file']
      filename=secure_filename(pdf.filename)
      basedir=os.path.abspath(os.path.dirname(__file__))
      pdf.save(os.path.join(basedir,app.config["PDF_uploads"],filename))
      #pdf.save(secure_filename(pdf.filename))
      res=access_file()
      ans,mismatch_font_style_out,min_lines_out=check(res)
      json_write(ans,mismatch_font_style_out, min_lines_out)
      delete_File(res)
      with open('static/sample.json', 'r') as myfile:
         data = myfile.read()
      return render_template("ans.html",jsonfile=json.dumps(data))



if __name__ == "__main__":
   app.config['TEMPLATES_AUTO_RELOAD'] = True
   app.run(debug=True)