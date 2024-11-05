texto = "Aula de Python"
for letra in texto:
    print(letra)



{
    'id': 'ORDE_0A38E06B-7711-45A4-9309-A64F65687071', 
    'reference_id': 'or0017', 
    'created_at': '2024-07-28T10:32:33.793-03:00', 
    'customer': {
        'name': 'Paulo Junior', 
        'email': 'npaulo_ce@yahoo.com.br', 
        'tax_id': '79715305016'}, 
    'items': [{
        'name': 'Plano Bronze', 
        'quantity': 1, 
        'unit_amount': 99900}], 
    'charges': [{
        'id': 'CHAR_921E9B58-4959-4523-ADBF-7AC66D5D834F', 
        'reference_id': '0001', 
        'status': 'WAITING', 
        'created_at': '2024-07-28T10:32:33.916-03:00', 
        'description': 'Descrição do Pagamento', 
        'amount': {
            'value': 99900, 
            'currency': 'BRL', 
            'summary': {
                'total': 99900, 
                'paid': 0, 
                'refunded': 0
                }        
        }, 
        'payment_response': {
            'code': '20000', 
            'message': 'SUCESSO'}, 
        'payment_method': {
            'type': 'BOLETO', 
            'boleto': {
                'id': '5022F056-2308-480C-9C6F-D179DDD74D0C', 
                'barcode': '03399853012970000024227020901016278150000015630', 
                'formatted_barcode': '03399.85301 29700.000242 27020.901016 2 78150000015630', 'due_date': '2024-07-30', 
                'instruction_lines': {}, 
                'holder': {
                    'name': 'Paulo Junior', 
                    'tax_id': '79715305016', 
                    'email': 'npaulo_ce@yahoo.com.br', 
                    'address': {
                        'region': 'Ceara', 
                        'city': 'Amontada', 
                        'postal_code': '62540000', 
                        'street': 'Rua 25', 
                        'number': '12345', 
                        'locality': 'Aracatiara', 
                        'country': 'BRA', 
                        'region_code': 'CE'}
                }
            }
        }, 
        'links': [
            {
                'rel': 'SELF', 
                'href': 'https://boleto.sandbox.pagseguro.com.br/5022f056-2308-480c-9c6f-d179ddd74d0c.pdf', 
                'media': 'application/pdf', 
                'type': 'GET'
            }, 
            {
                'rel': 'SELF', 
                'href': 'https://boleto.sandbox.pagseguro.com.br/5022f056-2308-480c-9c6f-d179ddd74d0c.png', 
                'media': 'image/png', 'type': 'GET'
            },
            {
                'rel': 'SELF', 
                'href': 'https://sandbox.api.pagseguro.com/charges/CHAR_921E9B58-4959-4523-ADBF-7AC66D5D834F', 
                'media': 'application/json', 
                'type': 'GET'
            }
        ]
    }], 
    'notification_urls': [], 
    'links': [{
        'rel': 'SELF', 
        'href': 'https://sandbox.api.pagseguro.com/orders/ORDE_0A38E06B-7711-45A4-9309-A64F65687071', 
        'media': 'application/json', 
        'type': 'GET'
        },
        {
            'rel': 'PAY', 
            'href': 'https://sandbox.api.pagseguro.com/orders/ORDE_0A38E06B-7711-45A4-9309-A64F65687071/pay', 
            'media': 'application/json', 
            'type': 'POST'
        }
    ]}