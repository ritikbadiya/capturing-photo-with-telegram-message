#!/usr/bin/env python3
import subprocess
import requests
import json
from PIL import Image
import time
# update your telegram bot token here
token = ""
update_id=1

#subprocess.run(['streamer','-f','jpeg','-o','image.jpeg'])

def send_photo(chat_id=1062414758):
    with open('image.jpeg', 'rb') as file_opened:
        method='sendPhoto'
        api_url='https://api.telegram.org/bot{}/{}'.format(token,method)
        params = {'chat_id': chat_id}
        files = {'photo': file_opened}
        resp = requests.post(api_url, params, files=files)
        file_opened.close()
    return resp



def receive_update():
    global update_id
    method='getUpdates'
    parameters={'offset':update_id,'allowed_updates':'message'}
    url='https://api.telegram.org/bot{}/{}'.format(token,method)
    res=requests.get(url,params=parameters)
    #-545845852
    if(len(res.json()['result'])>0):
        update_id=res.json()['result'][-1]['update_id']+1
    return(res.json()['result'])
    ml=res.json()['result']
    md={}
    for i in range(len(ml)):
        md[ml[i]['message']['from']['id']:ml[i]['message']['text'][1:]]
    return md


while True:
    md=receive_update()
    if len(md)>0 and md[-1]['message']['text']=='Photo':
        subprocess.run(['streamer','-f','jpeg','-o','image.jpeg'])
        #time.sleep(1)
        send_photo()
    time.sleep(1)
