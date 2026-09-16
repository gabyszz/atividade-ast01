class ProcessadorDeAcoes:

    def validar_dados(self, dados: dict) -> bool:
        return True

    def salvar_dados(self, dados: dict) -> bool:
        return True

    def executar_processo(self, dados: dict):
        if self.validar_dados(dados):
            self.salvar_dados(dados)
            return "Processo executado com sucesso"

        return "Falha na validação dos dados"