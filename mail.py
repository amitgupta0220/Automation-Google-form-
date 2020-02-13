from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib


def sendmail(to_email):  # image_path before payment_status

    from_email = ""                                                             #Enter your email
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "This is a confirmation message"
    msg['From'] = from_email
    msg['To'] = to_email

    content = MIMEText("Hello", 'plain')
    msg.attach(content)

    # # This example assumes the image is in the given directory
    # if payment_status == 'paid':
    #     fp = open(image_path, 'r+b')
    #     msgImage = MIMEImage(fp.read())
    #     fp.close()
    #     msg.attach(msgImage)

    response = {}
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as s:
            s.starttls()
            s.login(from_email, "")                                               #Enter password           
            print("Sending Mail:", to_email)
            s.sendmail(from_email, to_email, msg.as_string())
        response['email_status'] = "Success"
    except Exception as err:
        print(err)
        response['email_status'] = "Failed"

    return response
