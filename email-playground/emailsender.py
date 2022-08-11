from email import message
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'saplasumeet@gmail.com'
email['to'] = 's.sapla132@gmail.com'
email['subject'] = 'Python email sender'

email.set_content(html.substitute(name='Sumeet'), 'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('saplasumeet@gmail.com', 'wchtwktyakgdepbo')
    smtp.send_message(email)
    print('all good boss')
