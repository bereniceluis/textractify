# textractify
[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) ![issues](https://img.shields.io/github/issues/muichii/textractify.svg) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/muichii/textractify/blob/main/LICENSE) 


A website that uses Optical Character Recognition to extract text from scanned images. It is built as a Flask web app using OpenCV for image processing and tesseract for image recognition. It allows the user to upload an image, which is processed first to easily recognize text. The processed image is then passed onto tesseract which performs image recognition and outputs the text.

## Features
Image processing ensures that the text in that image is readable. It does so by first converting the image to grayscale and thresholding the image.

## Limitations
Tesseract has its own set of limitations. It fails to deliver when passed images of different fonts or when font sizes are too small. Though image processing eliminates the noise in images to an extent, extremely noisy images don't do well with tesseract. This app may not do well with bordered images either.

## Demo
Upload an image [here](textractify.herokuapp.com/upload) using one of the images in the [uploads folder](https://github.com/muichii/textractify/tree/main/static/uploads) to view a demo of the OCR in action!

## Screenshots
**Landing page**

![image](https://user-images.githubusercontent.com/86459271/146956600-6dc3c21b-c553-4174-9393-b25f8942482e.png)

**Upload section**

![image](https://user-images.githubusercontent.com/86459271/146956983-9fc8c5f1-4e46-4df4-a80d-706e71aac544.png)

**Uploading an image**

![image](https://user-images.githubusercontent.com/86459271/146957298-b404f220-b171-45f2-8a1d-b9109b927819.png)


**Result**

![image](https://user-images.githubusercontent.com/86459271/146957461-de0a0eb3-9fa1-46b4-9c79-99108f8d8c43.png)

## Getting Started 
This installation procedure assumes you are on a Windows system, and have `pip` , `bash` , and `python3.9` installed.

### Requirements
- [Git](https://git-scm.com)
- [Python 3.6 (or higher)](https://www.python.org)
- [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)

  Download windows executable file by clicking the hyper link titled **tesseract-ocr-w64-setup-v4.1.0.20190314.exe.** (for 64-bit version) A notification asking you to save an     exe file called “Tesseract-ocr-w64-setup-v4.1.0.20190314.exe” will appear. Save this .exe file wherever you have enough storage space. Open this exe file. If it windows         asks you “Do you want to allow this software to make changes to your system”, click yes. You will be taken to the installation section.

### Python Packages
- `Flask`
- `pytesseract`
- `Pillow`
- `opencv-python`

### **Steps to execute the app locally**
1. Download the project files:
   
   On, click the green "Clone or Download" button at the top right of the page. If you want to get started with this script more quickly, click the "Download ZIP" button, and      extract the ZIP somewhere on your computer.
   
   or you can clone using this command:
    ```
    git clone https://github.com/muichii/textractify.git
    cd textractify
    ```
    
2. Create a new virtual env:

    ```
    python3.9 -m venv venv
    ```
    
3. Activate the virtualenv:
    
    ```
    source venv/bin/activate
    ```
    
4. Install the project requirements:

    ```
    pip install -r requirements.txt
    ```
5. Run the Script:
    
    ```
    python app.py
    ```

6. Review the Results:
    
   The app.py script will start the python flask server.
   
   ```
   Serving on 127.0.0.1:5000
   ```

If the above steps does not work, download the zip file and extract it. Copy and paste the extracted folders on your desired code editor and install the project dependencies by doing step 4 and run the app.py script which will direct you to `localhost:5000`

## Note
- only `JPG`, `JPEG`, and `PNG` file formats are supported.
- all the image files uploaded in the local server are stored in `uploads` folder

## Website
[textractify](textractify.herokuapp.com) is already deployed and running on Heroku. The website might go on maintenance from time to time.  

## Technology Stack
#### Backend
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

#### Frontend
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white) 

#### Framework
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) 

#### Image Processing & OCR
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white) <a href='https://github.com/shivamkapasia0' target="_blank"><img alt='Tesseract' src='https://img.shields.io/badge/Tesseract-100000?style=for-the-badge&logo=Tesseract&logoColor=white&labelColor=0561FF&color=26A8E4'/></a>

#### Web Hosting
![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)
