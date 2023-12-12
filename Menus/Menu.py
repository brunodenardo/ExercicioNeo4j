from Menus.MenuUsuario import MenuUsuario
from Menus.MenuProduto import MenuProduto
from Menus.MenuCompra import MenuCompra
from Menus.MenuFavoritos import MenuFavoritos
from Menus.MenuHistorico import MenuHistorico

class Menu:

    menuUsuario = MenuUsuario()
    menuCompra = MenuCompra()
    menuProduto = MenuProduto()
    menuHistorico = MenuHistorico()
    menuFavoritos = MenuFavoritos()

    def menu(self, sessao):
        key=0
        while key != "S":
            print("\n--- Menu ---\n")
            print("1 - Menu Usuário")
            print("2 - Menu Produto")
            print("3 - Menu Favoritos")
            print("4 - Menu Compras")
            print("5 - Menu Histórico\n")

            key = input("Escolha uma das opções (S para sair): ")

            if key == "1":
                self.menuUsuario.menu(sessao)
            elif key == "2":
                self.menuProduto.menu(sessao)
            elif key == "3":
                self.menuFavoritos.menu(sessao)
            elif key == "4":
                self.menuCompra.menu(sessao)
            elif key == "5":
                self.menuHistorico.menu(sessao)
            else:
                print("\nOpção inválida\n")