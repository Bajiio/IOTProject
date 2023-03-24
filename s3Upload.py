import boto3
from pprint import pprint
import pathlib
from pathlib import Path
import sys
import os
import glob
import time
from botocore.exceptions import ClientError
from pictureAnalysis import detect_and_write_image

def upload_file_using_client(filename):
    """
    Uploads file to S3 bucket using S3 client object
    :return: None
    """
    response=None
    path = Path(filename)
    s3 = boto3.client("s3")
    bucket_name = "iot-project-lama2"
    object_name = path.name
    file_name = filename
    try:
    	response = s3.upload_file(file_name, bucket_name, object_name)
#	print(str(filename) + "send !")
    except ClientError as e:
       	logging.error(e)
#	print("Error, check logs to see the reasons")
       	return False
    return response
    
def getLastFile(path):
	files = list(filter(os.path.isfile, glob.glob(path)))
	# sort by modified time
	files.sort(key=lambda x: os.path.getmtime(x))
	lastfile=files[-2]
	return lastfile


time.sleep(1)
filename=getLastFile("/home/pi/cameraProject/shots/*")
detected=detect_and_write_image(filename)
filename = os.path.basename(filename)
if detected == 1:
	response=upload_file_using_client("/home/pi/resultProject/" + filename)
	if response == None:
		print("Upload Done!")
	cmd ="echo " +  filename + " >> /home/pi/cameraProject/uploadedPictures.txt"
	os.system(cmd)
else:
	print("Person Or Car Not Detected")
