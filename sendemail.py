from db import Database
from bucket import Bucket
db = Database()
bucket = Bucket()
import requests

# we are using mailgun to send email

class SendEmail:
    def __init__(self):
        self
    def send_email(self, plate_number, image):
        url = "https://api.mailgun.net/v3/sandboxf1feda92794145a9ae8e5a800b965ab4.mailgun.org/messages"

        to = db.getEmail(plate_number)

        content = f"""
        <html>
        <body>
        <h1>Violation Detected</h1>
        <p>Dear User,</p>
        <p>A violation has been detected with the number plate {plate_number}. Please find the image below.</p>
        <img src="{bucket.get_public_url(image)}" alt="Violation Detected" style="width:500px;height:500px;">
        <p>Regards,</p>
        <p>Team Traffic</p>
        </body>
        </html>
        """


        payload = {'from': 'mailgun@sandboxf1feda92794145a9ae8e5a800b965ab4.mailgun.org',
        'to': to,
        'subject': 'Violation Detected',
        'html': content}

        headers = {
        'Authorization': 'Basic YXBpOjRmMDViZGIwNmVjMTA5MDVhNzI3ZTgxYTM0OWNkMjVmLWY2OGEyNmM5LTAwNDMxZGZj'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)