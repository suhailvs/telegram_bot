from django.test import TestCase, Client
from django.urls import reverse

from .models import TelegramUser, CallCount

class TelegramBotTest(TestCase):
    # fixtures = ["datas.json"]

    def setUp(self):
        self.client = Client()
        self.button_response_from_telegram = '''{
    "update_id": 134884061,
    "callback_query": {
        "id": "1783103291429351918",
        "from": {
            "id": 415161087,
            "is_bot": false,
            "first_name": "Suhail",
            "username": "suhail_vs",
            "language_code": "en"
        },
        "message": {
            "message_id": 53,
            "from": {
                "id": 1449605051,
                "is_bot": true,
                "first_name": "Impress",
                "username": "impress_ai_bot"
            },
            "chat": {
                "id": 415161087,
                "first_name": "Suhail",
                "username": "suhail_vs",
                "type": "private"
            },
            "date": 1611684401,
            "text": "Yo Mama is so fat, when the cops see her on a street corner, they yell, Break it up!",
            "reply_markup": {
                "inline_keyboard": [
                    [{
                        "text": "Fat",
                        "callback_data": "fat"
                    }, {
                        "text": "Stupid",
                        "callback_data": "stupid"
                    }, {
                        "text": "Dumb",
                        "callback_data": "dumb"
                    }]
                ]
            }
        },
        "chat_instance": "-4531526532594316154",
        "data": "fat"
    }
}'''

        self.text_response_from_telegram = '''{
    "update_id": 134884062,
    "message": {
        "message_id": 56,
        "from": {
            "id": 415161087,
            "is_bot": false,
            "first_name": "Suhail",
            "username": "suhail_vs",
            "language_code": "en"
        },
        "chat": {
            "id": 415161087,
            "first_name": "Suhail",
            "username": "suhail_vs",
            "type": "private"
        },
        "date": 1611710359,
        "text": "S"
    }
}'''
    
        

    def test_homepage_displays_telegram_users(self):
        # make a dummy telegram button click post request 
        self.client.generic('POST', reverse('bot'), self.button_response_from_telegram)

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code,200)

        # there is html table in homepage and check there is user Suhail in the table
        table = f'''
        <tbody>            
            <tr>
                <td rowspan="2">415161087</td>
                <td rowspan="2">suhail_vs</td>
                <td rowspan="2">Suhail</td>                
            </tr>                
            <tr>
                <td>fat</td>
                <td>1</td>
            </tr>
        </tbody>'''

        # make a dummy telegram text message post request 
        self.client.generic('POST', reverse('bot'), self.text_response_from_telegram)
        
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code,200)
