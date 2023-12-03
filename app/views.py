import re
import base64
import flask

from werkzeug.exceptions import *
from flask import request, make_response, json
from app import app_flask
from app.service import *


PATH_DEFAULT = "/api/message"


@app_flask.errorhandler(HTTPException)
def handle_exception(e: HTTPException):
  return make_response(
    json.dumps({
        "code": e.code,
        "description": e.description,
    }), e.code
)
  
@app_flask.route(f"{PATH_DEFAULT}/wpp", methods=['POST'])
def send_msg_wpp():
  if request.method != 'POST':
    raise MethodNotAllowed
  
  data = request.get_json()
  
  if 'phone' not in data:
    return make_response({"error": "O campo 'phone' é obrigatório"}), 400
  
  phone = data['phone']
  
  if not validar_numero(phone):
    return make_response({'error': 'Número de Telefone Inválido', 'message': 'Exemplo: 5585912345678'}), 400
  
  enviar_mensagem(phone, message_template_cobrança)
  
  return make_response({"status" : "sucess", "message" : f"Mensagem enviada com Sucesso para o número {phone}"})
