import re
import os
import requests

from dotenv import load_dotenv

from flask import request, make_response
from app import mail, Message, app_flask

load_dotenv()
key = os.getenv('API_KEY')
phone_load = os.getenv('PHONE')

message_template_cobrança = 'Identificamos que você está com cobrança(s) em aberto\nSegue os links para acessar os boletos:'


def validar_numero(numero):
  padrao = r'^55\d{2}9\d{8}$'
  if re.match(padrao, numero):
      return True
  else:
      return False
    
def validar_message(message):
  return len(message) > 20
    
def enviar_mensagem(phone_send: str, message):
  url_send_msg = "https://app.whatsgw.com.br/api/WhatsGw/Send"
  
  payload_msg = {
    "apikey" : key,
    "phone_number" : phone_load,
    "contact_phone_number" : phone_send,
    "message_custom_id" : "yoursoftwareid",
    "message_type" : "text",
    "message_body" : f"{message}",
    "check_status" : "1"
  }
  
  headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
  }

  response = requests.request("POST", url_send_msg, headers=headers, data=payload_msg)
  
  if response.status_code != 200:
    return make_response({'error': 'Número de Telefone Inválido || Exemplo: 5585912345678'}), 400


def enviar_email(email: str, pdfs: list[str]):
  msg = Message('Cobrança IPTU', sender='nnoreply592@gmail.com', recipients=[email])
  msg.html = "<h1>Identificamos que você está com cobrança(s) em aberto</h1>" + "<br><br>"
  msg.html += "<h2>Segue os links para acessar os boletos:</h2><br>"
  msg.html += "<ul>"
  for pdf in pdfs:
        msg.html += pdf
  msg.html += "</ul>"
  mail.send(msg)