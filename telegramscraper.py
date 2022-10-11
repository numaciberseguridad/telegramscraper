#!/usr/bin/python

import requests
import argparse
import sys


text="Enviar texto de pruebas"
token = sys.argv[2]
chat_id = sys.argv[4]

url= f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"

r = requests.get(url)

print (r.json())
