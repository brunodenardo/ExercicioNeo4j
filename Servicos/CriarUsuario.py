from ConexaoNeoJ import ConexaoNeoJ
import json

class CriaUsuario:

    conexao = ConexaoNeoJ()

    def criar(self, sessao):
        dicionario = self.criaUsuario()
        sessao.execute_query(
            """MERGE (:Usuario {
                usuario_nome: $usuario_nome,
                usuario_email: $usuario_email, 
                usuario_senha: $usuario_senha,
                usuario_login: $usuario_login,
                usuario_telefone: $usuario_telefone,
                usuario_endereco: $usuario_endereco,
                usuario_pagamento: $usuario_pagamento})""",
            parameters_=dicionario,
            database_="neo4j",
        )

    def criaUsuario(self):
        print("\nCriação de Usuário\n")
        usuario = {}
        usuario["usuario_nome"] = input("Digite o nome do usuário: ")
        usuario["usuario_login"] = input("Digite o login do usuario: ")
        usuario["usuario_senha"] = input("Digite a senha do usuário: ")
        usuario["usuario_email"] = input("Digite o email do usuário: ")
        usuario["usuario_telefone"] = input("Digite o telefone do usuário: ")
        usuario["usuario_endereco"] = []
        resp = "sim"
        while resp == "sim":
            print("\nEndereço\n")
            endereco = {}
            endereco['endereco_bairro'] = input("Digite bairro do endereço: ")
            endereco['endereco_cep'] = input("Digite o cep do endereço: ")
            endereco['endereco_estado'] = input("Digite o estado do endereço: ")
            endereco['endereco_informacao_adicional'] = input("Digite as indoremações adicionais: ")
            endereco['endereco_numero'] = input("Digite o número do endereço: ")
            endereco['endereco_rua_avenida'] = input("Digite a rua e avenida do endereço: ")
            endereco['endereco_tipo'] = input("Digite o tipo do endereço: ")
            usuario["usuario_endereco"].append(endereco)
            resp = input("\nDeseja cadastrar mais um endereço (sim/não): ")
        resp = "sim"
        usuario["usuario_endereco"] = json.dumps(usuario["usuario_endereco"])
        usuario["usuario_pagamento"] =[]
        while resp =="sim":
            print("\nForma de Pagamento\n")
            pagamento = {}
            pagamento["pagamento_tipo"] = input("Digite o tipo de pagamento: ")
            pagamento["pagamento_cartao"] = input("Digite o número do cartão: ")
            usuario["usuario_pagamento"].append(pagamento)
            resp = input("Deseja cadastrar mais uma forma de pagamento (sim/não):  ")
        usuario["usuario_pagamento"] = json.dumps(usuario["usuario_pagamento"])
        return usuario