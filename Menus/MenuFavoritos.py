from Servicos.FavoritaProduto import FavoritaProduto
from Servicos.SelectFavoritos import SelectFavoritos

class MenuFavoritos:

    favoritador = FavoritaProduto()
    selecionador = SelectFavoritos()

    def menu(self, sessao):
        key = 0
        while key != "V":
            print("\n--- Menu Favoritos ---\n")

            print("1 - Favoritar um Produto")
            print("2 - Ver favoritos de um Usuário\n")

            key = input("Escolha uma das opções (V para voltar): ")

            if key == "1":
                self.favoritador.favoritar(sessao)
            elif key == "2":
                self.selecionador.listar(sessao)
            else:
                print("\nAção inválida\n")