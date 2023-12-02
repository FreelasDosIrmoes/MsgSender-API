import re

from werkzeug.exceptions import *
from flask import request
from app import *


PATH_DEFAULT = "/api/message"


@app.errorhandler(HTTPException)
def handle_exception(e: HTTPException):
  return make_response(
    json.dumps({
        "code": e.code,
        "description": e.description,
    }), e.code
)
  
@app.route(f"{PATH_DEFAULT}/wpp/<phone>", methods=['POST'])
def send_msg_wpp(phone: str):
  if request.method != 'POST':
    raise MethodNotAllowed
      
  if not validar_numero(phone):
    return jsonify({'erro': 'Número de Telefone Inválido || Exemplo: 5585912345678'}), 400
  
  return make_response('aaa')
    
