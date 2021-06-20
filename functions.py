#function to send a mail with the photo and name of the first person

#for making this work you'll have to enable your gmail for less secure apps
#1. Open your Google Admin Console or "Manage your account"
#2. Security -> Less Secure apps
#3. Turn it on. It will display warning. Make sure not to use this code publically to expose your password!


def email(name):
    destid='mail_id'       # put the destination mail id here
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    
    
    fromm = "mail_id"                 #put the name of mail id you'll use to send the mail
    to = destid

    # instance of MIMEMultipart
    data = MIMEMultipart()

    # storing the senders email address  
    data['From'] = fromm

    # storing the receivers email address 
    data['To'] = to

    # storing the subject 
    data['Subject'] = "Sneak Alert"

    # string to store the body of the mail
    body = "Person detected in front of camera: "+name

    # attach the body with the msg instance
    data.attach(MIMEText(body, 'plain'))

    # open the file to be sent 
    filename = "mail.jpg"
    attachment = open('mail.jpg', "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    
    # attach the instance 'p' to instance 'msg'
    data.attach(p)
    
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!Warning!!!!!!!!!!!!!!!!!!!!!!!!!!
    #!!Make sure to remove password before using it publically!!!!!
    s.login(fromm, "password")                           #set password for authentication

    # Converts the Multipart msg into a string
    text = data.as_string()

    # sending the mail
    
    print('sending email to rahul18bhardwaj.23@gmail.com')
    s.sendmail(fromm, to, text)

    # terminating the session
    s.quit()







#function to send whatsapp
#install pywhatkit library to use this code with ```pip install pywhatkit```

def sendwhatsappmssg():
    print('running sendwhatsappmsg')
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    #print("Current Time =", current_time)
    type(current_time)
    h=current_time[:2]
    m=current_time[3:5]
    h=int(h)
    m=int(m)
    
    print('about to send whatsapp message')
    import pywhatkit as pwk
    pwk.sendwhatmsg('<phone_no>','Whatsapp message sent from python!',h,m+1.3)


#function to launch an aws instance with a 5GiB EBS volume attached to it.
import json
import subprocess
def awslaunch():
    x=subprocess.getoutput(aws_cmd)
    y=json.loads(x)
    print('An instance with id:', y['Instances'][0]['InstanceId'], ' launched at :',y['Instances'][0]['LaunchTime'], 'with 5GiB EBS storage')
   
aws_cmd="aws ec2 run-instances --image-id ami-0ad704c126371a549 --instance-type t2.micro --subnet-id subnet-8d6168e5 --security-group-ids sg-07673146644fec545 --key-name mykey --block-device-mapping file://directory_where_you_kept_mapping.json/mapping.json"

