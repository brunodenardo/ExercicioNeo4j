from Servicos.InsertHistorico import InsertHistorico
from Servicos.SelectHistorico import SelectHistorico

class MenuHistorico:

    guardador = InsertHistorico()
    selecionador = SelectHistorico()

    def menu(self, sessao):
        key = 0
        while key != "V":
            print("\n--- Menu Histórico ---\n")

            print("1 - Guardar um Produto no Histórico")
            print("2 - Ver o histórico de um Usuário\n")

            key = input("Escolha uma das opções (V para voltar): ")

            if key == "1":
                self.guardador.guardarHistorico(sessao)
            elif key == "2":
                self.selecionador.listar(sessao)
            else:
                print("\nAção inválida\n")