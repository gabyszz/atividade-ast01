class CarrinhoDeCompras:

    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def remover_item(self, item):
        if item not in self.itens:
            raise ValueError("Item não encontrado")

        self.itens.remove(item)

    def listar_itens(self):
        return self.itens