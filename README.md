# face-recog-whatsapp-email-aws-instance
This repo consists of LBPH face recognition code that recognises first person's face and send a whatsapp message and email with the picture of person detected with his/her name. On recognizing second person it launches an ec2 instance with 5GiB volume attached to it.

## How to use this repo
* Keep all the above files in the same folder (except pywhatkit_dbs.txt. This file will be created automatically to keep the logs of the messages sent through whatsapp)
* Go to functions.py and fill the credentials for sending email and whatsapp. Go through the instructions provided in the comments.
* Run the sample1.py file to take the sample images of person from your webcam.
* Run the sample2.py file to take the sample images of second person from your webcam.
* Run the main.py file with the first person in front of webcam.
* It will run the email() and sendwhatsappmssg() simultaneously. 
* For sending whatsapp message it will open whatsapp web. Note: Do not minimise the window when you're text has been printed on the text bar of window. You can set the timing in the code to automatically send the message.
* You can check the email in the destination id's inbox.
* Bring the second person in front of camera. 
* A message about launching the instance will pop with some configurations about the instance.
* And its done!

## Sample1/2.py
This file uses haarcascade to detect the face in the image, crops the face from it, turns it into black and white, resizes it into 200x200 and saves it into a repo. It uses the same cropped image, puts the sample number on it shows it on your screen.

## S
