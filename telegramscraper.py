#!/usr/bin/python

import requests
import argparse
import sys

Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--text", help="Text to send in the message")
parser.add_argument("-tok", "--token", help="Telegram bot token")
parser.add_argument("-cid", "--chat_id", help="Telegram chat ID")
args = parser.parse_args()

Set default values for arguments
text = args.text or "Enviar texto de pruebas"
token = args.token
chat_id = args.chat_id

Check if required arguments are provided
if not token or not chat_id:
print("Error: Telegram bot token and chat ID are required arguments.")
exit()

Create URL for API request
url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"

Send API request and print response
r = requests.get(url)
print(r.json())
