from Servicos.SelecionaUsuario import SelecionaUsuario
from Servicos.SelecionaProduto import SelecionaProduto
from Servicos.InputNumerico import InputNumerico


class CompraProduto:

    selecionadorProduto = SelecionaProduto()
    selecionadorUsuario = SelecionaUsuario()
    inputNumerico = InputNumerico()

    def comprar(self, sessao):
        id_usuario = self.selecionadorUsuario.selecionarId(sessao, "comprar")
        id_produto = self.selecionadorProduto.selecionarId(sessao, "ser comprado")
        sessao.execute_query("""
            MATCH (u:Usuario) WHERE id(u) = $id_usuario
            MATCH (p:Produto) WHERE id(p) = $id_produto
            MERGE (u)-[:COMPRA]->(p)
        """, id_usuario=id_usuario, id_produto=id_produto,)