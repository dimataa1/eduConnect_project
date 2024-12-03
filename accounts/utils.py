from django.template.loader import render_to_string
from mailjet_rest import Client
from django.conf import settings


def send_welcome_email(email, username):
    mailjet = Client(auth=(settings.MAILJET_API_KEY, settings.MAILJET_SECRET_KEY), version='v3.1')
    html_content = render_to_string('common/email-greeting.html', {'username': username})

    data = {
        'Messages': [
            {
                "From": {
                    "Email": "dimitar200720@gmail.com",
                    "Name": "eduConnect"
                },
                "To": [
                    {
                        "Email": email,
                        "Name": username
                    }
                ],
                "Subject": "Welcome to EduConnect!",
                "TextPart": "Greetings from our platform!",
                "HTMLPart": html_content
            }
        ]
    }

    result = mailjet.send.create(data=data)
    return result.status_code, result.json()


def send_teacher_approval_email(email, username):
    mailjet = Client(auth=(settings.MAILJET_API_KEY, settings.MAILJET_SECRET_KEY), version='v3.1')

    # Load the HTML content from the template
    html_content = render_to_string('accounts_structure/approved_teacher.html', {'username': username})

    data = {
        "Messages": [
            {
                "From": {
                    "Email": "dimitar200720@gmail.com",
                    "Name": "eduConnect"
                },
                "To": [
                    {
                        "Email": email,
                        "Name": username
                    }
                ],
                "Subject": "Your Teacher Account Has Been Approved!",
                "TextPart": "We are pleased to inform you that your teacher account has been approved.",
                "HTMLPart": html_content
            }
        ]
    }

    result = mailjet.send.create(data=data)
    return result