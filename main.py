import functions       #user-defined module
import train           #user-defined module
import threading
import time
import cv2


face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        
def face_detector(img, size=0.5):
    
    # Convert image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []
    
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi

def cam():
    cap=cv2.VideoCapture(0)
    rflag=0
    hflag=0
    while True:
            
        ret, frame = cap.read()

        image, face = face_detector(frame)
        
        try:

            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            # Pass face to prediction model
            # "results" comprises of a tuple containing the label and the confidence value   
            results1 = train.person1_model.predict(face)

            if results1[1] < 500:
                confidence = int( 100 * (1 - (results1[1])/400) )
                display_string = str(confidence) + '% Confident it is User'
                flag=1

            cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)

            if confidence > 90:
                cv2.imwrite('mail.jpg', image)
                cv2.putText(image, "Hey Person 1", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                cv2.imshow('Face Recognition', image )


                if rflag==0:
                 
                    x3=threading.Thread(target=functions.sendwhatsappmssg)
                    x5=threading.Thread(target=functions.email, args=["Person 1"])
                    x5.start()
                    x3.start()
                    rflag=rflag+1
                    #print('incremented flag:',rflag)
                    pass

            else:
                cv2.imshow('Face Recognition', image )

        except:
            cv2.imshow('Face Recognition', image )
            pass
        
        #for second person
        try:
            # Pass face to prediction model
            # "results" comprises of a tuple containing the label and the confidence value

            results2 = train.person2_model.predict(face)

            if results2[1] < 500:
                confidence = int( 100 * (1 - (results2[1])/400) )
                display_string = str(confidence) + '% Confident it is User'

            cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)

            if confidence > 90:
                cv2.putText(image, "Hey Person 2", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                cv2.imshow('Face Recognition', image )
                if hflag==0:
                    print('launching aws and attaching ebs volume to it...')
                    x6=threading.Thread(target=functions.awslaunch)
                    x6.start()
                    hflag=hflag+1

            else:
                cv2.imshow('Face Recognition', image )

        except:
            cv2.imshow('Face Recognition', image )
        if cv2.waitKey(1) == 13:
            break

    cv2.destroyAllWindows()
    cap.release()
        

x4=threading.Thread(target=cam)
x4.start()