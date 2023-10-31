"""
from datetime import datetime

hora_atual = datetime.now()
h = hora_atual.strftime("%H")
h_completo = hora_atual.strftime("%H:%M:%S")
my_dict = {
    "manha":"bom dia!",
    "tarde":"boa tarde",
    "noite":"boa noite"
}

if int(h) >= 1 and int(h) < 12:
    print('São exatamente: ',h_completo, " tenha um " ,my_dict["manha"])
elif int(h) >=12 and int(h) < 18:
    print('São exatamente: ',h_completo, " tenha uma " ,my_dict["tarde"])
else:
    print('São exatamente: ',h_completo, " tenha uma " ,my_dict["noite"])
"""

cadastro = {
    'nome':'Paulo',
    'enderco': 'Rua 01',
    }

print(cadastro.items())
