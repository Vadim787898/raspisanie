import vk_api
import time
import random
import json
import datetime
from datetime import date
from datetime import datetime
import pytz
token = "c77899d1d0c1279854dd9e5c1ef40c1c77f119de5466a12cd05b2f0781579a48d4a90fec437230bb7096b"
vk = vk_api.VkApi(token=token)
vk._auth_token()
from vk_api import VkApi, AuthError
from vk_api.utils import get_random_id
a=[222533355] #Андрей 301
b=[239951631, 273201522] #Максим и Я 302
c=[232684037] #Серёга 308 
d=[630727918, 314337501] #Борис и Сергей 318
e=[170581884, 243009689] #Рома и Дима 303
f=[313946405, 634364802] #Саня 305
g=[445164085, 552458776] #Айдар и Иван 306
h=[203633112, 288715883] #Дима и Дима 307
kj=[a, b, c, d, e, f, g, h]
#op=[301, 302, 303, 305, 306, 307, 308, 318]
op=[301, 302, 308, 318, 303, 305, 306, 307]
def send_message(vk_session, user_id, message):  
    try:  
        vk_session.method('messages.send', {  
            'user_id': user_id,  
             'message': message,  
              'random_id': get_random_id()  
         })
    except AuthError as e:  
        print(f'Ошибка авторизации: {e}')  
    except Exception as e:  
        print(f'Ошибка отправки сообщения: {e}')
vk_session = VkApi(token='c77899d1d0c1279854dd9e5c1ef40c1c77f119de5466a12cd05b2f0781579a48d4a90fec437230bb7096b', api_version='5.131')
keyboard = {
"one_time" : False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Продежурил"
            },
            "color": "positive"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Нет возможности продежурить"
            },
            "color": "negative"
        }
    ],
    [
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Дежурит следующая комната"
            },
            "color": "positive"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Какая комната сегодня дежурит?"
            },
            "color": "positive"
        }
        ]
    ]
}
keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))
zx=0
lk=0
nodij=0
qw=1
while True:
    if zx==len(kj):
        zx=0
    data = date.today()
    data=str(data)
    god=int(data[0:4])
    mesyc=int(data[5:7])
    den=int(data[8:10])
    date=datetime(god, mesyc, den)
    tz = pytz.timezone('Indian/Kerguelen')
    current_time = datetime.now(tz)
    if current_time.hour<=6:
        df=1
    else:
        df=0
    if date.isoweekday()==1 or date.isoweekday()==2 or date.isoweekday()==3 or date.isoweekday()==4 or date.isoweekday()==5 or (date.isoweekday()==6 and df==1) or (date.isoweekday()==7 and df==0):
        if current_time.hour==22 and current_time.minute==0 and current_time.second==0:
            qw=0
            for i in range(len(kj[zx])):
                send_message(vk_session, kj[zx][i], "Пора дежурить")
        try:
            messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
            tz = pytz.timezone('Indian/Kerguelen')
            current_time = datetime.now(tz)
            if messages["count"] >= 1:
                id = messages["items"][0]["last_message"]["from_id"]
                body = messages["items"][0]["last_message"]["text"]
                if body.lower()=="дежурит следующая комната" and (id==273201522 or id==232684037):
                    if zx==len(kj)-1:
                        zx=0
                    else:
                        zx=zx+1
                    vk.method("messages.send", {"peer_id": id, "message": "Назначена на дежурство комната " + str(op[zx]),  "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
                if body.lower()=="какая комната сегодня дежурит?":
                    vk.method("messages.send", {"peer_id": id, "message": "Сегодня дежурит комната " + str(op[zx]),  "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
                if len(kj[zx])==1:
                    if body.lower() == "продежурил" and id==kj[zx][0] and (current_time.hour>=22 or current_time.hour<=5):
                        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                        keyboard = str(keyboard.decode('utf-8'))
                        qw=qw+1
                        vk.method("messages.send", {"peer_id": id, "message": "Отлично",  "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
                        if qw==1:
                            lk=1
                    elif body.lower() == "продежурил" and id!=kj[zx][0]:
                        vk.method("messages.send", {"peer_id": id, "message": "Сейчас не ваша очередь", "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
                else:
                    if body.lower() == "продежурил" and (id==kj[zx][0] or id==kj[zx][1]) and (current_time.hour>=22 or current_time.hour<=5):
                        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                        keyboard = str(keyboard.decode('utf-8'))
                        qw=qw+1
                        vk.method("messages.send", {"peer_id": id, "message": "Отлично",  "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
                        if qw==1:
                            lk=1
                    elif body.lower() == "продежурил" and (id!=kj[zx][0] or id!=kj[zx][1]):
                        vk.method("messages.send", {"peer_id": id, "message": "Сейчас не ваша очередь", "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
                if len(kj[zx])==1:
                    if body.lower() == "нет возможности продежурить" and id==kj[zx][0]:
                        vk.method("messages.send", {"peer_id": id, "message": "Хорошо", "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
                        nodij=nodij+1
                    elif body.lower() == "нет возможности продежурить" and id!=kj[zx][0]:
                        vk.method("messages.send", {"peer_id": id, "message": "Сейчас не ваша очередь", "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
                else:
                    if body.lower() == "нет возможности продежурить" and (id==kj[zx][0] or id==kj[zx][1]):
                        vk.method("messages.send", {"peer_id": id, "message": "Хорошо", "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
                        nodij=nodij+1
                    elif body.lower() == "нет возможности продежурить" and (id!=kj[zx][0] or id!=kj[zx][1]):
                        vk.method("messages.send", {"peer_id": id, "message": "Сейчас не ваша очередь", "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
                if nodij==len(kj[zx]):
                    nodij=0
                    zx=zx+1
                    for i in range(len(kj[zx])):
                        send_message(vk_session, kj[zx][i], "У другой комнаты нет возможности продежурить, поэтому дежурите вы")
                elif current_time.hour==6 and current_time.minute==0 and current_time.second==0:
                    if lk==0:
                        for i in range(len(kj[zx])):
                            send_message(vk_session, kj[zx][i], "Вы в бане")
                        send_message(vk_session, 232684037, "Не продежурила комната " + str(op[zx]))
                    else:
                        lk=0
                        zx=zx+1
                        time.sleep(1)
                oldmessage = body.lower()
            if body.lower()=="lk=1":
                lk=1
                vk.method("messages.send", {"peer_id": id, "message": "Окей", "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
            if body.lower()=="состояние переменных":
                print('lk', lk)
                print('qw', qw)
                print('df', df)
                vk.method("messages.send", {"peer_id": id, "message": "Ok", "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
        except Exception as E:
            time.sleep(1)
    else:
        try:
            messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
            if messages["count"] >= 1:
                    id = messages["items"][0]["last_message"]["from_id"]
                    body = messages["items"][0]["last_message"]["text"]
                    if body.lower()=="продежурил" or body.lower()=="нет возможности продежурить" or body.lower()=="дежурит следующая комната" or body.lower()=="какая комната сегодня дежурит?":
                        vk.method("messages.send", {"peer_id": id, "message": "В субботу никто не дежурит, поэтому бот неактивен", "keyboard": keyboard, "random_id": random.randint(1, 2147483647)})
        except Exception as E:
            time.sleep(1)
            
