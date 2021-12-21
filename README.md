# textractify
[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/muichii/textractify/blob/main/LICENSE) 


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

## Pre-requisites
This installation procedure assumes you are on a Windows system, and have `pip` , `bash` , and `python3.9` installed.
### Requirements
- [Git](https://git-scm.com)
- [Python 3.6 (or higher)](https://www.python.org)
- [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)

### Python Packages
- `Flask`
- `pytesseract`
- `Pillow`
- `opencv-python`


### Steps
