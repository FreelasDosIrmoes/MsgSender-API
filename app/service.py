import re
import os
import requests
import jsonify

from dotenv import load_dotenv

load_dotenv()
key = os.getenv('API_KEY')

message_template_cobrança = 'Identificamos que você está com cobrança(s) aberta(s)\n segue anexos:'


def validar_numero(numero):
  padrao = r'^55\d{2}9\d{8}$'
  if re.match(padrao, numero):
      return True
  else:
      return False
    
def validar_message(message):
  return len(message) > 20
    
def enviar_mensagem(phone_send: str, message: str):
  url_send_msg = "https://app.whatsgw.com.br/api/WhatsGw/Send"
  
  phone_current = '5585989427436'

  payload_msg={
  "apikey" : key,
  "phone_number" : phone_current,
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
    return jsonify({'erro': 'Número de Telefone Inválido || Exemplo: 5585912345678'}), 400
