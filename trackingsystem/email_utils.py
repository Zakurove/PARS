from django.core.mail import send_mail

def send_email(subject, message, recipient_list):
    send_mail(subject, message, 'your-email@example.com', recipient_list)
