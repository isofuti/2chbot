import random
import discord
from discord import webhook, RequestsWebhookAdapter
from discord import Webhook

WEBHOOK_ID = '' #don't forget to insert
WEBHOOK_TOKEN = '' #don't forget to insert
webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter())

class WebHook():

    def random_pic():

        piclist = [
            'C:/Users/Professional/Desktop/animepic/pic.png',
            'C:/Users/Professional/Desktop/animepic/unnamed.jpg',
            'C:/Users/Professional/Desktop/animepic/16272953781160.png',
            'C:/Users/Professional/Desktop/animepic/16272398202303.jpg',
            'C:/Users/Professional/Desktop/animepic/16272281200690.jpg',
            'C:/Users/Professional/Desktop/animepic/be20446a33015be07863330480ec3189--tag-polyvore.jpg',
            'C:/Users/Professional/Desktop/animepic/ccdeaa0aa1a833a352d5f5194181c95e.jpg',
            'C:/Users/Professional/Desktop/animepic/d8275d0b892dd9d5cfbee0990e6261d4.jpg',
            'C:/Users/Professional/Desktop/animepic/b05043a47b2f36e01f840b419c4653cf.jpg'
        ]
        randpic = random.choice(piclist)

        return randpic

    def create_content(flist: list, wlist: list):

        content = ''

        if len(flist) != 0:
            content = content + '**С пометкой FAP!**@everyone\n'
            for i, item in enumerate(flist):
                hr = str(flist[i])
                content = content + hr + '\n'

        if len(wlist) != 0:
            content = content + '**С пометкой WEBM!**@everyone\n'
            for i, item in enumerate(wlist):
                hr = str(wlist[i])
                content = content + hr + '\n'
        
        return content

    def send_hook(faplist, webmlist):

        hook = WebHook.create_content(faplist, webmlist)

        f= discord.File(WebHook.random_pic())
        webhook.send(content= hook, username='2chBot', avatar_url='https://yt3.ggpht.com/a/AGF-l78AYoX8Tvp0jpJS0A0Dd2N4P1sJwRFkLXfarA=s900-c-k-c0xffffffff-no-rj-mo', file=f)
