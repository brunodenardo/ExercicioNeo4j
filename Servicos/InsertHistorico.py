from Servicos.SelecionaUsuario import SelecionaUsuario
from Servicos.SelecionaProduto import SelecionaProduto
from Servicos.InputNumerico import InputNumerico


class InsertHistorico:

    selecionadorProduto = SelecionaProduto()
    selecionadorUsuario = SelecionaUsuario()
    inputNumerico = InputNumerico()

    def guardarHistorico(self, sessao):
        id_usuario = self.selecionadorUsuario.selecionarId(sessao, "colocar o Produto no Histórico")
        id_produto = self.selecionadorProduto.selecionarId(sessao, "guardar no Histórico")
        sessao.execute_query("""
            MATCH (u:Usuario) WHERE id(u) = $id_usuario
            MATCH (p:Produto) WHERE id(p) = $id_produto
            MERGE (u)-[:HISTORICO]->(p)
        """, id_usuario=id_usuario, id_produto=id_produto,)