import json
from django.core.mail import send_mail

def send_notification(channel, method, properties, body):
    print(f"Received message: {body}")
    print(f"Message properties: {properties}")

    data = json.loads(body)

    if data["status"] == "failed":
        #send email to user
        email_user = data["email"]
        subject = "Video processing failed for the following video: " + data["name"]
        message = "Video processing failed for the following video: " + data["name"]
        send_mail(subject, message, email_user, [email_user])
