from Servicos.CriarUsuario import CriaUsuario
from Servicos.SelecionaUsuario import SelecionaUsuario
from pprint import pprint

class MenuUsuario:

    selecionador = SelecionaUsuario()
    criaUsuario = CriaUsuario()

    def menu(self, sessao):
        key=0
        while key != "V":
            print("\n--- Menu Usuário ---\n")
            print("1 - Criar Usuário")
            print("2 - Listar Usuários")
            print("3 - Detalhar Usuário\n")


            key = input("Escolha uma das opções (V para voltar): ")

            if key == "1":
                self.criaUsuario.criar(sessao)
            elif key == "2":
                pprint(self.selecionador.listarTodos(sessao))
            elif key == "3":
                self.selecionador.detalhaUsuario(sessao)
            else:
                print("\nAção inválida\n")