idade = int(input("Por favor digite sua idade: "))

if idade <= 2 or idade >=8 and idade <= 60:
    bpm = int(input("Por favor digite sua frequência cardiáca: "))
    if idade <= 2 and bpm >= 120 and bpm <= 140:
        print("Dentro da faixa adequada")
    elif idade <= 2 and bpm < 120:
        print("Abaixo da faixa adequada")
    elif idade <= 2 and bpm > 140:
        print("Acima da faixa adequada")
    elif idade >= 8 and idade < 18 and bpm >= 80 and bpm <= 100:
        print("Dentro da faixa adequada")
    elif idade >= 8 and idade < 18 and bpm < 80:
        print("Abaixo da faixa adequada")
    elif idade >= 8 and idade < 18 and bpm > 100:
        print("Acima da faixa adequada")
    elif idade >= 18 and idade < 60 and bpm >= 70 and bpm <= 80:
        print("Dentro da faixa adequada")
    elif idade >= 18 and idade < 60 and bpm < 70:
        print("Abaixo da faixa adequada")
    elif idade >= 18 and idade < 60 and bpm > 80:
        print("Acima da faixa adequada")
    elif idade >= 60 and bpm >= 50 and bpm <= 60:
        print("Dentro da faixa adequada")
    elif idade >= 60 and bpm < 50:
        print("Abaixo da faixa adequada")
    elif idade >= 60 and bpm > 60:
        print("Acima da faixa adequada")
else: print("Não é possível realizar o cálculo para essa idade")

