import re
import os
import requests
import jsonify
import json  
import base64

from dotenv import load_dotenv

from flask import request, make_response
from app import mail, Message, app_flask

load_dotenv()
key = os.getenv('API_KEY')
phone_load = os.getenv('PHONE')

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
  
  payload_msg={
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
    return jsonify({'error': 'Número de Telefone Inválido || Exemplo: 5585912345678'}), 400

def enviar_pdf_wpp(phone_send: str, pdf):
  url_send_pdf = "https://app.whatsgw.com.br/api/WhatsGw/Send"
  payload = json.dumps({
    "apikey": key,
    "phone_number": phone_load,
    "contact_phone_number": phone_send,
    "message_custom_id": "yoursoftwareid",
    "message_type": "document",
    "check_status": "1",
    "message_body_mimetype": "application/pdf",
    "message_body_filename": "RelatorioDAR.pdf",
    "message_caption": "",
    "message_body": f"{pdf}"})
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url_send_pdf, headers=headers, data=payload)   
  
  if response.status_code != 200:
    return jsonify({'error': 'Aconteceu algum erro ao enviar os PDFs'}), 400

def enviar_email(email: str, pdf, attached_pdfs):
  msg = Message('Cobrança IPTU', sender='nnoreply592@gmail.com', recipients=[email])
  msg.body = 'Identificamos que você está com cobrança(s) aberta(s)\n segue anexos:'
  
  for pdf_data in attached_pdfs:
        pdf_filename = pdf_data['filename']
        pdf_content_base64 = pdf_data['content']
        
        pdf_content = base64.b64decode(pdf_content_base64)
        
        msg.attach(pdf_filename, 'application/pdf', pdf_content)
  
  mail.send(msg)