from flask import Flask, render_template, request
# from flask.templating import DispatchingJinjaLoader
from werkzeug.utils import secure_filename
import os
from PIL import Image
import pytesseract
import cv2


__source__ = ''

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = './static/uploads'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
# app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# route and function to handle the home page
@app.route("/")
def index():
  return render_template("index.html")


# route and function to handle the upload page
@app.route('/upload', methods = ['GET', 'POST'])
def upload():
  if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        # create a secure filename
    
        file = request.files['file']

        # create a secure filename
        filename = secure_filename(file.filename)

        # save file to /static/uploads
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):
            image = cv2.imread(filepath)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            tresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
            ofilename = os.path.join(app.config['UPLOAD_FOLDER'],"{}.png".format(os.getpid()))
            cv2.imwrite(ofilename, gray)
            # extract the text and display it
            extracted_text = pytesseract.image_to_string(Image.open(ofilename))

            return render_template('upload.html',
                                   extracted_text=extracted_text,
                                   img_src=UPLOAD_FOLDER + file.filename)
  elif request.method == 'GET':
    return render_template('upload.html')


@app.route("/privacy-policy")
def privacy_policy():
    return render_template("policy.html")

if __name__ == '__main__':
   app.run(port= 777, debug= True)

