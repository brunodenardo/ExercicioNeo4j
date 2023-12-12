from Servicos.SelecionaUsuario import SelecionaUsuario
from Servicos.SelecionaProduto import SelecionaProduto
from Servicos.InputNumerico import InputNumerico
from pprint import pprint

class FavoritaProduto:

    selecionadorProduto = SelecionaProduto()
    selecionadorUsuario = SelecionaUsuario()
    inputNumerico = InputNumerico()

    def favoritar(self, sessao):
        id_usuario = self.selecionadorUsuario.selecionarId(sessao, "favoritar o Produto")
        id_produto = self.selecionadorProduto.selecionarId(sessao, "ser favoritado")
        sessao.execute_query("""
            MATCH (u:Usuario) WHERE id(u) = $id_usuario
            MATCH (p:Produto) WHERE id(p) = $id_produto
            MERGE (u)-[:FAVORITOU]->(p)
        """, id_usuario=id_usuario, id_produto=id_produto,)
