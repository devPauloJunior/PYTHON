from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("O cpf deve conter 11 digitos")
        return cpf  
    
    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError("Não colocar numeros no campo do nome")
        return nome
    
    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError("O rg deve conter 9 digitos")
        return rg
   
    def validate_celular(self, celular):
        if len(celular) != 11:
            raise serializers.ValidationError("O numero de celular deve conter 11 digitos")
        return celular

