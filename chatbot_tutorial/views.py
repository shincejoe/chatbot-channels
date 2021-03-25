from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from django.shortcuts import render
import os
from mocker.models import Clicks, Users


def chat(request):
    context = {}
    return render(request, 'chatbot_tutorial/chatbot.html', context)


def respond_to_websockets(message):
    jokes = {
        'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                   """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
        'fat': ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                """Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, 
                break it up!" """],
        'dumb': ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked 
     for extra thick.""",
                 """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""]
    }
    # div element for displaying the buttons for fat, dumb and Stupid
    div = '<div class="centre custom-center"><div class=""><button class="btn btn-primary cust-btn" value="fat" ' \
          'onclick="sendBtnMessage(\'''fat''\')" id="fat">Fat </button><button class="btn btn-primary cust-btn"  ' \
          'onClick="sendBtnMessage(\'''stupid''\')" id="stupid">Stupid</button><button ' \
          'class="btn btn-primary cust-btn" onClick="sendBtnMessage(\'''dumb''\')" id="dumb">Dumb</button></div></div>'

    # added a disable_send_btn variable for deciding when to enable\disable the buttons
    result_message = {
        'type': 'text',
        'options': None,
        'disable_send_btn': False
    }
    user_obj = Users.objects.filter(pk=int(message['user_id'])).first()
    print(message['text'])
    print(message['user_id'])
    if 'fat' in message['text']:
        result_message['text'] = random.choice(jokes['fat'])
        # sending the div element for buttons to client-side and updating the counts for "fat" button
        result_message['options'] = div
        result_message['disable_send_btn'] = True
        fat_obj = Clicks.objects.filter(type=1, user=user_obj).first()
        if fat_obj:
            fat_obj.count = fat_obj.count + 1
            fat_obj.save()
        else:
            fat_obj = Clicks(type=1, count=1, user=user_obj)
            fat_obj.save()
    elif 'stupid' in message['text']:
        # sending the div element for buttons to client-side and updating the counts for "stupid" button

        result_message['text'] = random.choice(jokes['stupid'])
        result_message['options'] = div
        result_message['disable_send_btn'] = True
        stupid_obj = Clicks.objects.filter(type=2, user=user_obj).first()
        if stupid_obj:
            stupid_obj.count = stupid_obj.count + 1
            stupid_obj.save()
        else:
            stupid_obj = Clicks(type=2, count=1, user=user_obj)
            stupid_obj.save()
    elif 'dumb' in message['text']:
        # sending the div element for buttons to client-side and updating the counts for "dumb" button

        result_message['text'] = random.choice(jokes['dumb'])
        result_message['options'] = div
        result_message['disable_send_btn'] = True
        dumb_obj = Clicks.objects.filter(type=3, user=user_obj).first()
        if dumb_obj:
            dumb_obj.count = dumb_obj.count + 1
            dumb_obj.save()

        else:
            dumb_obj = Clicks(type=3, count=1, user=user_obj)
            dumb_obj.save()

    elif message['text'] in ['hi', 'hey', 'hello']:
        result_message['text'] = "Hello "+str(user_obj.username) +", If you're interested in yo mama jokes, just tell me fat, " \
                                 "stupid or dumb and i'll tell you an appropriate joke. "
        result_message['options'] = div
        result_message['disable_send_btn'] = True
    else:
        result_message['text'] = "I don't know any responses for that. If you're interested in yo mama jokes tell me " \
                                 "fat, stupid or dumb. "
        result_message['options'] = div
        result_message['disable_send_btn'] = True

    return result_message
