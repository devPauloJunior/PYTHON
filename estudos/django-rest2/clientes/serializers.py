from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"O CPF deve conter 11 digitos"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não colocar numeros no campo do NOME"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve conter 9 digitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O numero de celular deve conter 11 digitos"})
        return data