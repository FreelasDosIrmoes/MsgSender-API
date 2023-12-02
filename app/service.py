import re

def validar_numero(numero):
  padrao = r'^55\d{2}9\d{8}$'
  if re.match(padrao, numero):
      return True
  else:
      return False
    
    