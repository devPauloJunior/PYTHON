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

    def __setitem__(self, index, value):
        if index <= len(self.lista):
            self.lista[index] = value
        else:
            raise IndexError()

    def __contains__(self, value):
        return value in self.lista

    def append(self, value):
        self.lista.append(value)

    def __repr__(self):
        return str(self.lista)

    def __add__(self, outra_lista):
        return ListaCustomizada(self.lista + outra_lista.lista)

minha_lista = ListaCustomizada()
minha_lista.append(1)
minha_lista.append(2)
minha_lista.append(3)
minha_lista.append(4)
minha_lista.append(5)
print(len(minha_lista))
print(minha_lista[3])
minha_lista[3] = 100
print(minha_lista[3])
print(4 in minha_lista)
print(minha_lista)
outra_lista = ListaCustomizada()
outra_lista.append(1000)
outra_lista.append(2000)
print(outra_lista)
print(minha_lista + outra_lista)