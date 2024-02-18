import re
import flask

from werkzeug.exceptions import *
from flask import request, make_response, json
from app import app_flask
from app.service import *
from time import sleep

PATH_DEFAULT = "/api/messages"


@app_flask.errorhandler(HTTPException)
def handle_exception(e: HTTPException):
  return make_response(
    json.dumps({
        "code": e.code,
        "description": e.description,
    }), e.code
)
  
@app_flask.route(f"{PATH_DEFAULT}", methods=['POST'])
def send_msgs():
  if request.method != 'POST':
    raise MethodNotAllowed

  data = request.get_json()
  
  if 'phone' not in data:
    return make_response({"error": "O campo 'phone' é obrigatório"}), 400
  
  if 'pdf' not in data:
    return make_response({"error": "O campo 'pdf' é obrigatório"}), 400
  
  if 'email' not in data:
    return make_response({"error": "O campo 'email' é obrigatório"}), 400
  
  phone = data['phone']
  pdf = data['pdf']
  email = data['email']

  if not validar_numero(phone):
    return make_response({'error': 'Número de Telefone Inválido', 'message': 'Exemplo: 5585900000000'}), 400
  
  enviar_mensagem(phone, message_template_cobrança)
  for p in pdf:
    enviar_mensagem(phone, p)
  
  enviar_email(email, pdf)
  
  return make_response({"status" : "sucess", "message" : f"Mensagens enviadas com Sucesso para o número {phone} e email {email}"})

@app_flask.route(f"{PATH_DEFAULT}/wpp", methods=['POST'])
def send_msg_wpp():
  if request.method != 'POST':
    raise MethodNotAllowed
  
  data = request.get_json()
  
  if 'phone' not in data:
    return make_response({"error": "O campo 'phone' é obrigatório"}), 400
  
  if 'pdf' not in data:
    return make_response({"error": "O campo 'phone' é obrigatório"}), 400
  
  phone = data['phone']
  pdf = data['pdf']
  
  if not validar_numero(phone):
    return make_response({'error': 'Número de Telefone Inválido', 'message': 'Exemplo: 5585912345678'}), 400
  
  enviar_mensagem(phone, message_template_cobrança)
  for p in pdf:
    enviar_mensagem(phone, p)

  return make_response({"status" : "sucess", "message" : f"Mensagem enviada com Sucesso para o número {phone}"})

@app_flask.route(f"{PATH_DEFAULT}/email", methods=['POST'])
def send_msg_email():
  if request.method != 'POST':
    raise MethodNotAllowed
  
  data = request.get_json()
  
  if 'email' not in data:
    return make_response({"error": "O campo 'phone' é obrigatório"}), 400
  
  if 'pdf' not in data:
    return make_response({"error": "O campo 'phone' é obrigatório"}), 400
  
  email = data['email']
  pdf = data['pdf']
  
  enviar_email(email, pdf)
  
  return make_response({"status" : "sucess", "message" : f"Mensagem enviada com Sucesso para o email {email}"})
