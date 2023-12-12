from Servicos.CompraProduto import CompraProduto
from Servicos.SelectCompras import SelectCompras

class MenuCompra:

    comprador = CompraProduto()
    selecionador = SelectCompras()

    def menu(self, sessao):
        key = 0
        while key != "V":
            print("\n--- Menu Compras ---\n")

            print("1 - Comprar um Produto")
            print("2 - Ver as compras de um Usuário\n")

            key = input("Escolha uma das opções (V para voltar): ")

            if key == "1":
                self.comprador.comprar(sessao)
            elif key == "2":
                self.selecionador.listar(sessao)
            else:
                print("\nAção inválida\n")