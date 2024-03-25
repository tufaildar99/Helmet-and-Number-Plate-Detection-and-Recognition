from bucket import Bucket
from sendemail import SendEmail 
from db import Database
db = Database()
bucket = Bucket()
sendemail = SendEmail()

sendemail.send_email('PBP3H 0298', '52b86d81-04c1-4885-b2ce-af184521c5d4.png')