# face-recog-whatsapp-email-aws-instance
This repo consists of LBPH face recognition code that recognises first person's face and send a whatsapp message and email with the picture of person detected with his/her name. On recognizing second person it launches an ec2 instance with 5GiB volume attached to it.

Follow this link to see demo: [face-recog-whatsapp-email-aws-instance](https://www.linkedin.com/posts/bhardwaj-rahul_internship-aws-summer-activity-6812743957651435520-yuxw)

## How to use this repo
* Keep all the above files in the same folder (except pywhatkit_dbs.txt. This file will be created automatically to keep the logs of the messages sent through whatsapp)
* Go to functions.py and fill the credentials for sending email and whatsapp. Go through the instructions provided in the comments.
* Run the sample1.py file to take the sample images of person from your webcam.
* Run the sample2.py file to take the sample images of second person from your webcam.
* Run the main.py file with the first person in front of webcam.
* It will run the email() and sendwhatsappmssg() simultaneously. 
* For sending whatsapp message it will open whatsapp web. **Note:** Do not minimise the window when you're text has been printed on the text bar of window. You can set the timing in the code to automatically send the message.
* You can check the email in the destination id's inbox.
* Bring the second person in front of camera. 
* A message about launching the instance will pop with some configurations about the instance.
* And its done!

## Prerequisites
* Install pywhatkit, and opencv-contrib-python.

## Sample1/2.py
This file uses haarcascade to detect the face in the image, crops the face from it, turns it into black and white, resizes it into 200x200 and saves it into a repo. It uses the same cropped image, puts the sample number on it shows it on your screen.

## Train.py
This repo is imported in the main.py file and will run automatically once the main.py file is started. This file will read the samples taken by sample1/2.py file with file handling, creates a numpy array of images and labels and train our dataset with the help of LBPHFaceRecognizer.

## Functions.py
This file consists all the functions for sending whatsapp message, emailing and launching aws instance with 5GiB EBS volume attached to it. 
* **sendwhatsappmssg()** : This function first uses datetime to find the current time and store the hour and minutes in "h" and "m" respectively. The main code to send the whatsapp message is ```pwk.sendwhatmsg('<phone_no>','Whatsapp message sent from python!',h,m+1.3)```. We increased the m by 1.3 minutes because sometimes the time provided is insufficient for the function to initialize.
* **email()**: When the main.py file is done and the first person is detected and shown on the windows screen a copy of that image is simultaneously being saved in mail.jpg file. This function picks that file as an attachement only once when it is triggered and send it to destination mail id. For using attachment in our mail we used MIMEMultipart for this. We also typed in the name of the person 1 being shown on camera with the help of MIMEText. We then used MIMEBase as the base object to set octect stream, setting up payload. We then started the ttls with SMTP send the message an quit the session.
* **awslaunch()**: This function uses subprocess and run the aws cli command. To run this function you should be having the mapping.json file present in the folder.

## Main.py
This file will first import the functions.py and train.py and with that it will train the models for both the persons automatically. We then created a function face_detector() in it which will take a photo use haarcascade to detect face and send back the image with a cropped part of it containing the face in gray color. After that we have the main function cam(). This function will run in a infinite while loop and capture the image, send it to face_detector and get back the cropped image so that we can use it for our model's prediction. For the first part of the while loop we first test it with the first person's model and store the result in some variable. We then convert this result out of hundred to make a confidence score. If the confidence score is more than 90 its flag will incremented once and the email and sendwhatsappmssg functions will be triggered only once. If the image fails to predict it will show errror for which we used error handling and will move on to the except part and will just show the captured image. After this in the same while loop it will run in the same manner for the second person and if the confidence is above 90 aws launch functions will be triggered. 

Now, doing this will create problem as the functions triggered will stop the ongoing imshow functions and will crash the window showing the camera. For this we put the whole cam() in one thread and all the three triggered functions in individual separated threads. Like this they will operate independently without disturbing other processes. 



And that's it your program is sending mails and launching aws instances.
