from Trivago.trivago import Trivago

lugar = 'Curitiba'
entrada = '2025-04-15'
saida = '2025-04-20'

adultos = 3
pet = True
quartos = 3


with Trivago() as bot:
    bot.homepage()
    # bot.trocaMoeda("USD")
    bot.pesquisar(lugar, entrada, saida)
    bot.passageiros(adultos, quartos, pet)
    print("\n-------------------------------------")
    bot.resultados()
    print("-------------------------------------")
    print("\n-------------------------------------")
    input("Aperte enter para finalizar o codigo\n-------------------------------------\n")
    print("FINALIZANDO...")