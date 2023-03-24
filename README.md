# IOTProject
ISEN IOT Project Cyber

# Summary :

1. s3upload.py : It is the main script, define function which find last picture taken and can upload picture to s3 bucket, this script is started by Motion
2. pictureAnalysis.py : It define a function which the main script use, this function call and send pictures to rekognition in order to get labels and then analyse these to draw or not bounding-box.
3. testImage.py : a script that take a picture path in argument and analyse it. Output reveals if a result picture has been created.

# Usage:

## Don't forget to change the folder path where result pictures are written (end of pictureAnalysis.py) and were the upload script retrieve the picture to send to s3
Download file, unzip and start s3upload.py 
To test if a picture is recognized by rekognition, you can use .... script this way : `python testImage.py <path to img to test here>`
