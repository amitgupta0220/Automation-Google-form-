from file_utils import read_csv, write_csv, read_file, write_file
from generate import _render_template, preprocess
from mail import sendmail
import json
from Test import getMail

getMail()
data = read_csv()
# Reading the scraped data from the csv and preprocessing the data
participants = data
participants = preprocess(participants)

#Getting the list of mails to whom mails have already been sent
sent_mails = read_file()
# Looping over all participants
for participant in participants:
    # Checking if the participant was sent a mail previously
    if participant['email'] not in sent_mails:
        #name = participant['name']
        email = participant['email']

        # Generating a message from the template
       # message = _render_template()
        # Generating a custom image
        #image_path = pass_gen(name, email, phone)
        
        # Sending the message to the participant via mail
        response = sendmail(email)  #image_path before payment_status
        print(response)

        if response['email_status'] == "Success":
            # if mail was sent successfully append the email to sentmails.txt
            write_file(participant['email'])
