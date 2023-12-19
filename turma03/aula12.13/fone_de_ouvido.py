class FoneDeOuvido:

    def get_volume(self):
        print('Entrei no GET')
        return self.__volume
    
    def set_volume(self, novo_volume):
        print(f'Entrei no SET com o volume de { novo_volume }')
        self.__volume = novo_volume

    volume = property(get_volume, set_volume)

fone = FoneDeOuvido()

fone.volume = 200 # SET

print(fone.volume) # GET