from Servicos.SelecionaUsuario import SelecionaUsuario
from pprint import pprint

class SelectCompras:

    selecionadorUsuario = SelecionaUsuario()

    def listar(self, sessao):
        id_usuario = self.selecionadorUsuario.selecionarId(sessao, "ver as Compras")
        records, summary, keys = sessao.execute_query("""
            MATCH (u:Usuario) WHERE id(u) = $id
            MATCH (u:Usuario)-[:COMPRA]->(p:Produto)
            RETURN p
        """, id=id_usuario)
        produtos = []
        for record in records:
            produtos.append(record.data()["p"])
        
        pprint(produtos)