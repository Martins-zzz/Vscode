from OOP_Contas import *

Cleiton = conta(1000, "Cleiton")
Alberto = conta(500, "Alberto")
Cleiton.deposito(22)
Cleiton.Consultar
Cleiton.saque(1000)
Cleiton.Consultar()
Alberto.transferir(500, Cleiton)
Alberto.Consultar()
Cleiton.Consultar()