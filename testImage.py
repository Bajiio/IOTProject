from pictureAnalysis import detect_and_write_image
import sys

check = detect_and_write_image(sys.argv[1])
if check == 1:
    print("Person or car detected, result in ~/projectResult/")
else:
    print("Person or car not detected, no result built")
