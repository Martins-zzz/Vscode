class problema(Exception):
    pass
class conta:
    def __init__(self, valorInicial, nomeConta):
        self.saldo = valorInicial
        self.nome = nomeConta
        print(f"\nConta '{self.nome}' Iniciada\nSaldo: '{self.saldo:.2f}'")
    
    def Consultar(self):
        print(f"\nSaldo Atual '{self.saldo:.2f}'")

    def deposito(self, x):
        self.saldo = self.saldo + x
        print(f"Valor Depositado")

    def possivel(self, x):
        if x <= self.saldo:
            return
        else:
            raise problema(f"\nA Conta Possui Apenas '{self.saldo:.2f}'")
        
    def saque(self, x):
        try:
            self.possivel(x)
            self.saldo = self.saldo - x
            print("\nSaque completo")
        except problema as error:
            print(f"\nSaque interrompido {error}")

    def transferir(self, x, acc):
        try:
            self.saque(x)
            acc.deposito(x)
        except problema as error:
            print(f'Transferencia interrompida {error}')
        print("Transferencia concluida")