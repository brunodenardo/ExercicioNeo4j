from Servicos.CriaProduto import CriaProduto
from Servicos.SelecionaProduto import SelecionaProduto
from pprint import pprint

class MenuProduto:
   
   criaProduto = CriaProduto()
   selecionador = SelecionaProduto()

   def menu(self, sessao):
        key=0
        while key != "V":
            print("\n--- Menu Produto ---\n")
            print("1 - Criar Produto")
            print("2 - Listar Produto")
            print("3 - listar Produtos vendidos por um Usuário\n")


            key = input("Escolha uma das opções (V para voltar): ")

            if key == "1":
                self.criaProduto.criar(sessao)
            elif key == "2":
                pprint(self.selecionador.listarTodos(sessao))
            elif key == "3":
                self.selecionador.listarPorVendedor(sessao)
            else:
                print("\nAção inválida\n")