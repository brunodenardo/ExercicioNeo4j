from Servicos.InputNumerico import InputNumerico
from pprint import pprint
import json

class SelecionaUsuario:

    inputNumerico = InputNumerico()

    def listarTodos(self, sessao):
        records, summary, keys = sessao.execute_query("""
            MATCH (p:Usuario) RETURN id(p) AS id, p.usuario_nome AS nome, p.usuario_email AS email
        """, database_="neo4j",)
        lista = []
        numero = 0
        for resposta in records:
            resposta = resposta.data()
            resposta["numero"] = numero
            numero += 1
            lista.append(resposta)
        return lista


    def selecionarId(self, sessao, acao):
        lista = self.listarTodos(sessao)
        pprint(lista)
        indice = self.inputNumerico.inputIntLista(f"Escolha o número do Usuario que pretende {acao}: ", len(lista))
        id  = lista[indice]["id"]
        return id
    
    def detalhaUsuario(self, sessao):
        lista = self.listarTodos(sessao)
        pprint(lista)
        indice = self.inputNumerico.inputIntLista(f"Escolha o número do Usuário que pretende detalhar: ", len(lista))
        id  = lista[indice]["id"]
        records, summary, keys = sessao.execute_query("""
            MATCH (p:Usuario) WHERE id(p) = $id RETURN p 
        """, id=id)
        usuario = records[0].data()["p"]
        usuario["usuario_endereco"] = json.loads(usuario["usuario_endereco"])
        usuario["usuario_pagamento"] = json.loads(usuario["usuario_pagamento"])
        pprint(usuario)