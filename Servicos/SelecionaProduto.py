from Servicos.InputNumerico import InputNumerico
from Servicos.SelecionaUsuario import SelecionaUsuario
from pprint import pprint

class SelecionaProduto:

    seleciodnadorUsuario = SelecionaUsuario()
    inputNumerico = InputNumerico()

    def listarTodos(self, sessao):
        records, summary, keys = sessao.execute_query("""
            MATCH (p:Produto) RETURN id(p) AS id, p
        """, database_="neo4j",)
        lista = []
        numero = 0
        for resposta in records:
            produto = {}
            resposta = resposta.data()
            produto = resposta["p"]
            id = resposta["id"]
            produto["id"] = id
            produto["numero"] = numero
            numero += 1
            lista.append(produto)
        return lista


    def selecionarId(self, sessao, acao):
        lista = self.listarTodos(sessao)
        pprint(lista)
        indice = self.inputNumerico.inputIntLista(f"Escolha o número do Produto que pretende {acao}: ", len(lista))
        id  = lista[indice]["id"]
        return id
    
    def detalhaProduto(self, sessao):
        lista = self.listarTodos(sessao)
        pprint(lista)
        indice = self.inputNumerico.inputIntLista(f"Escolha o número do Produto que pretende detalhar: ", len(lista))
        id  = lista[indice]["id"]
        records, summary, keys = sessao.execute_query("""
            MATCH (p:Produto) WHERE id(p) = $id RETURN p 
        """, id=id)
        pprint(records[0].data()["p"])

    def listarPorVendedor(self, sessao):
        id_usuario = self.seleciodnadorUsuario.selecionarId(sessao, "ver os Produtos a venda")
        records, summary, keys = sessao.execute_query("""
            MATCH (u:Usuario) WHERE id(u) = $id
            MATCH (u)-[:VENDE]->(p:Produto)
            RETURN p
        """, id=id_usuario)
        produtos = []
        for record in records:
            produtos.append(record.data()["p"])
        pprint(produtos)

        