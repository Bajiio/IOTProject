from PIL import Image, ImageDraw
import os
import boto3

def detect_and_write_image(path):
    # Set up Rekognition client
    rekognition = boto3.client('rekognition' , region_name='us-east-1')

    # Load image file
    with open(path, 'rb') as image_file:
        image_bytes = image_file.read()

    # Call Rekognition detect_labels API
    response = rekognition.detect_labels(
        Image={
            'Bytes': image_bytes
        },
        MaxLabels=5,
        MinConfidence=50.0
    )

    # allowed label names
    allowed_labels = ['Person', 'Car']

    # filter labels by name
    labels = response['Labels']
    filtered_labels = [label for label in labels if label['Name'] in allowed_labels]

#    print(str(response) + "\n")
#    print("FILTERED LABEL:\n" + str(filtered_labels))

    #result = json.loads(filtered_labels)

    # Open the JPEG image file
    image = Image.open(path)
    image_size = image.size

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    #labels = result['Labels']
    checkIfDone=0
    for label in filtered_labels:
        if label['Name'] == "Person":
            checkIfDone=1
            for instance in label['Instances']:
                width = instance['BoundingBox']['Width'] * image_size[0]
                height = instance['BoundingBox']['Height'] * image_size[1]
                left = instance['BoundingBox']['Left'] * image_size[0]
                top = instance['BoundingBox']['Top'] * image_size[1]

                # Define the coordinates of the rectangle
                x1, y1 = (left, top)  # Top left corner
                x2, y2 = (left + width, top + height)  # Bottom right corner

                # Draw the rectangle on the image
                draw.rectangle((x1, y1, x2, y2), outline="red", width=5)

                draw.text((x1 + 10, top + 10), "Humain", fill=(255, 0, 0))

        if label['Name'] == "Car":
            checkIfDone=1
            for instance in label['Instances']:
                width = instance['BoundingBox']['Width'] * image_size[0]
                height = instance['BoundingBox']['Height'] * image_size[1]
                left = instance['BoundingBox']['Left'] * image_size[0]
                top = instance['BoundingBox']['Top'] * image_size[1]

                # Define the coordinates of the rectangle
                x1, y1 = (left, top)  # Top left corner
                x2, y2 = (left + width, top + height)  # Bottom right corner

                # Draw the rectangle on the image
                draw.rectangle((x1, y1, x2, y2), outline="blue", width=5)

                draw.text((x1 + 10, top + 10), "Voiture", fill=(0, 0, 255))

    if checkIfDone==1:
        # Convert the image to RGB mode
        image = image.convert("RGB")
        filename = os.path.basename(path)
        # Save the modified image
        image.save("/home/pi/resultProject/" + filename)
    return checkIfDone
