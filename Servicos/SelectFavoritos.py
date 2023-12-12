from Servicos.SelecionaUsuario import SelecionaUsuario
from pprint import pprint

class SelectFavoritos:

    selecionadorUsuario = SelecionaUsuario()

    def listar(self, sessao):
        id_usuario = self.selecionadorUsuario.selecionarId(sessao, "ver os Favoritos")
        records, summary, keys = sessao.execute_query("""
            MATCH (u:Usuario) WHERE id(u) = $id
            MATCH (u:Usuario)-[:FAVORITOU]->(p:Produto)
            RETURN p
        """, id=id_usuario)
        produtos = []
        for record in records:
            produtos.append(record.data()["p"])
        
        pprint(produtos)