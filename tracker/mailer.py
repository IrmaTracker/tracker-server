import requests
from django.conf import settings


class MG(object):
    """
    MailGun mailer
    """
    def __init__(self):
        self.base_api_url = 'https://api.mailgun.net/v3/{}/messages'
        self.domain_name = 'mg.vokality.com'
        self.api_url = self.base_api_url.format(self.domain_name)
        self.api_key = getattr(settings, 'MAILGUN_API_KEY')
        self.email_user = getattr(settings, 'MAILGUN_EMAIL_USER')

    def send(self, subject, recipient, text):
        auth = ('api', self.api_key)
        data = {
            'from': self.email_user,
            'to': recipient,
            'subject': subject,
            'text': text
        }
        response = requests.post(self.api_url, data=data, auth=auth)
        return response
