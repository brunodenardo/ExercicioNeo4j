from Servicos.InputNumerico import InputNumerico
from Servicos.SelecionaUsuario import SelecionaUsuario


class CriaProduto:

    inputNumerico = InputNumerico()
    selecionadorUsuario = SelecionaUsuario()

    def criar(self, sessao):
        dicionario = self.criaProduto(sessao)
        sessao.execute_query("""
            MATCH (p:Usuario ) WHERE id(p) = $id_vendedor
            MERGE (p)-[:VENDE]->(:Produto {
                produto_descricao: $produto_descricao, 
                produto_nome: $produto_nome,
                produto_oferta: $produto_oferta, 
                produto_preco: $produto_preco
            })
            """, parameters_=dicionario,
            database_="neo4j",)



    def criaProduto(self, sessao):
        produto ={}
        produto["id_vendedor"] = self.selecionadorUsuario.selecionarId(sessao, "vender o Produto")
        produto["produto_nome"] = input("Digite o nome do produto: ")
        produto["produto_descricao"] = input("Digite a descricao do produto: ")
        produto["produto_preco"] = self.inputNumerico.inputFloat("Digite o preço: ")
        produto["produto_oferta"] = self.inputNumerico.inputInt("Digite a porcentagem de desconto (só número inteiro): ")
        return produto