import imaplib
import base64
import os
import email

email_user = 'carminaruizllaurado@gmail.com'
email_pass = 'ribes2005'


mail = imaplib.IMAP4_SSL('imap.gmail.com',993)
mail.login(email_user, email_pass)
print('he fet login')
mail.select('Inbox')
type, data = mail.search(None, '(UNSEEN SUBJECT "Recepta de cuina")')
print('inbox i mandangues')
mail_ids = data[0]
id_list = mail_ids.split()
print ('he fet idsplit')
for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)' )
    raw_email = data[0][1]# converts byte literal to string removing b''
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)# downloading attachments
    """for part in email_message.walk():
        # this part comes from the snipped I don't understand yet... 
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()


        if bool(fileName):
            filePath = os.path.join('/Users/sanketdoshi/python/', fileName)
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
            subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
            print('Downloaded "{file}" from email titled "{subject}" with UID {uid}.'.format(file=fileName, subject=subject, uid=latest_email_uid.decode('utf-8')))
"""
    for response_part in data:
        print('estic a un for xulo')
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1].decode('utf-8'))
            email_subject = msg['subject']
            email_from = msg['from']
            print ('From : ' + email_from + '\n')
            print ('Subject : ' + email_subject + '\n')
            print(msg.get_payload(decode=True))             