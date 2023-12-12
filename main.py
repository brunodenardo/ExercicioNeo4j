
from ConexaoNeoJ import ConexaoNeoJ
from Menus.Menu import Menu


conexao = ConexaoNeoJ()
menu = Menu()

sessao = conexao.conectar()
menu.menu(sessao)
sessao.close()


