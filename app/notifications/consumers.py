import json
from django.core.mail import send_mail

def send_notification(channel, method, properties, body):
    print(f"Received message: {body}")
    print(f"Message properties: {properties}")

    data = json.loads(body)

    email_user = data["email"]
    subject = "Video processing failed for the following video: " + data["video_name"]
    message = f"The video {data['video_name']} failed to process. reason: {data['reason']}"
    send_mail(subject, message, email_user, [email_user])
