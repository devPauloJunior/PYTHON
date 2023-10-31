class ListaCustomizada():
    def __init__(self, lista=None):
        if lista is None:
            self.lista = []
        else:
            self.lista = lista
    
    def __len__(self):
        return len(self.lista)
    
    def __getitem__(self, index):
        return self.lista[index]

    def __setitem__(self, index, valor):
        if index <= len(self.lista):
            self.lista[index] = valor
        else:
            raise IndexError()

    def __contains__(self, valor):
        return valor in self.lista

    def append(self, valor):
        self.lista.append(valor)
    
    def __repr__(self):
        return str(self.lista)

    def __add__(self, outra_lista):
        return ListaCustomizada(self.lista + outra_lista.lista)


minha_lista = ListaCustomizada()
minha_lista.append(2)
minha_lista.append(4)
minha_lista.append(6)
minha_lista.append(8)
minha_lista.append(10)
print(minha_lista)
print(len(minha_lista))
print(minha_lista[4])
minha_lista[4] = 100
print(minha_lista[4])
print(minha_lista)
print(8 in minha_lista)
print(40 in minha_lista)
print("*"*20)
outra_lista = ListaCustomizada()
outra_lista.append(20)
outra_lista.append(40)
print(outra_lista)
print(minha_lista + outra_lista + minha_lista)