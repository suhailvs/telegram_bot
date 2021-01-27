import json
import requests
import random
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from django.http import HttpResponse
from django.views import generic
from django.conf import settings

from .models import TelegramUser, CallCount


# TELEGRAM_USERNAME = "impress_ai_bot"

class TelegramUserList(generic.ListView):
    model = TelegramUser


class TelegramBotView(generic.View):
    def update_callcount_and_get_text(self, data):   
        if 'callback_query' not in data.keys():            
            return ''

        callback_query = data['callback_query']
        from_user = callback_query.get('from')

        telegram_user, _ = TelegramUser.objects.get_or_create(
            telegram_id = from_user.get('id'), 
            defaults={'username':from_user.get('username',''), 'firstname':from_user.get('first_name','')}
        )
        button = callback_query.get('data')

        call_count, _ = CallCount.objects.get_or_create(user=telegram_user, button=button)
        call_count.count += 1
        call_count.save()

        text = callback_query.get('message','')
        return {'chat_id':text.get('chat').get('id'), 'text':button}


    def send_messages(self, message):    
        jokes = {
         'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                    """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
         'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                    """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
         'dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                    """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""] 
        }  

        result_message = {'chat_id': message['chat_id']}  # the response needs to contain just a chat_id and text field for telegram to accept it
        
        if 'fat' in message['text']:
            result_message['text'] = random.choice(jokes['fat'])
        
        elif 'stupid' in message['text']:
            result_message['text'] = random.choice(jokes['stupid'])
        
        elif 'dumb' in message['text']:
            result_message['text'] = random.choice(jokes['dumb'])

        else:
            result_message['text'] = "I don't know any responses for that. If you're interested in yo mama jokes tell me fat, stupid or dumb."
        
        result_message['reply_markup'] = InlineKeyboardMarkup([
            [
                InlineKeyboardButton('Fat', callback_data='fat'),
                InlineKeyboardButton('Stupid', callback_data='stupid'),
                InlineKeyboardButton('Dumb', callback_data='dumb')
            ]
        ]).to_dict()

        requests.post(f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage", 
            headers={"Content-Type": "application/json"}, data=json.dumps(result_message))
   
            
    # Post function to handle messages in whatever format they come
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))

        # if no button is clicked on telegram app. ie typed a message 
        if 'message' in data.keys():
            # get text message from telegram        
            text_from_telegram = {'chat_id':data['message']['from']['id'], 'text':data['message']['text']}
        
        # if a button is clicked on telegram app.
        else:
            text_from_telegram = self.update_callcount_and_get_text(data)

        self.send_messages(text_from_telegram)
        return HttpResponse()

