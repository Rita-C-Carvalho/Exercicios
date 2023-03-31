categoria = int(input("Escolha categoria de sua viagem: "
                  "<1> Econômica"
                  "<2> Executiva"
               "<3> Primeira Classe"))
viajantes = int(input("Por favor digite a quantidade de pessoas que irá nesta viagem: "))
valorBruto = float(input("Digite o valor bruto de cada viagem: "))
valorBrutoPacote = valorBruto * viajantes
desconto = 0

if(categoria == 1 and viajantes == 2):
    desconto = 3 / 100
elif(categoria == 1 and viajantes == 3):
    desconto = 4 / 100
elif(categoria == 1 and viajantes >= 4):
    desconto = 5 / 100
elif(categoria == 2 and viajantes == 2):
    desconto = 5 / 100
elif(categoria == 2 and viajantes == 3):
    desconto = 7 / 100
elif(categoria == 2 and viajantes >= 4):
    desconto = 8 / 100
elif(categoria == 3 and viajantes == 2):
    desconto = 10 / 100
elif(categoria == 3 and viajantes == 3):
    desconto = 15 / 100
elif(categoria == 3 and viajantes >= 4):
    desconto = 20 / 100

valorDesconto = valorBrutoPacote * desconto
valorLiquido = valorBrutoPacote - valorDesconto
valorMedio = valorLiquido / viajantes
print("Valor bruto: {}".format(valorBruto) + "\n" +
      "Valor bruto pacote: {}".format(valorBrutoPacote) + "\n" +
      "Valor do desconto: {}".format(valorDesconto) + "\n" +
      "Valor líquido: {}".format(valorLiquido) + "\n" +
      "Valor médio por viajante: {}".format(valorMedio))


