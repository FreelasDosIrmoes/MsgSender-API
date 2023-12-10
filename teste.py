import base64
import requests
import json

# Carregar o PDF como bytes
with open('RelatorioDAR1.pdf', 'rb') as file:
    pdf1 = file.read()
with open('RelatorioDAR2.pdf', 'rb') as file:
    pdf2 = file.read()
with open('RelatorioDAR3.pdf', 'rb') as file:
    pdf3 = file.read()

# Codificar o PDF para base64

pdf_base64_1 = base64.b64encode(pdf1).decode('utf-8')
pdf_base64_2 = base64.b64encode(pdf2).decode('utf-8')
pdf_base64_3 = base64.b64encode(pdf3).decode('utf-8')

# URL da API de destino
url = 'http://localhost:5000/api/messages/wpp'

# Dados JSON que você deseja enviar
dados_json = {'pdf': pdf_base64_3, 'phone': '5585991230398'}

# Enviar a requisição POST com os dados
resposta = requests.post(url, json=dados_json)

# Verifica a resposta da API
if resposta.status_code == 200:
    print('Arquivo enviado com sucesso!')
else:
    print(f'Erro ao enviar arquivo. Código de status: {resposta.status_code}')
    print(resposta.text)