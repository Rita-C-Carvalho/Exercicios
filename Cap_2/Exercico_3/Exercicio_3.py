voto1 = int(input("Por favor informe o prêmio que deseja ganhar: "
                  "<1> Playstation"
                  "<2> Xbox"
                  "<3> Nitendo"))
voto2 = int(input("Por favor informe o prêmio que deseja ganhar: "
                  "<1> Playstation"
                  "<2> Xbox"
                  "<3> Nitendo"))
voto3 = int(input("Por favor informe o prêmio que deseja ganhar: "
                  "<1> Playstation"
                  "<2> Xbox"
                  "<3> Nitendo"))
voto4 = int(input("Por favor informe o prêmio que deseja ganhar: "
                  "<1> Playstation"
                  "<2> Xbox"
                  "<3> Nitendo"))
voto5 = int(input("Por favor informe o prêmio que deseja ganhar: "
                  "<1> Playstation"
                  "<2> Xbox"
                  "<3> Nitendo"))

playstation = 0
xbox = 0
nintendo = 0

if voto1 == 1:
    playstation = playstation+1
elif voto1 == 2:
    xbox = xbox+1
elif voto1 == 3:
    nintendo = nintendo+1
else:
    print("O colaborador 1 digitou um console inexistente e seu voto será desconsiderado")

if voto2 == 1:
    playstation = playstation+1
elif voto2 == 2:
    xbox = xbox+1
elif voto2 == 3:
    nintendo = nintendo+1
else:
    print("O colaborador 2 digitou um console inexistente e seu voto será desconsiderado")

if voto3 == 1:
    playstation = playstation+1
elif voto3 == 2:
    xbox = xbox+1
elif voto3 == 3:
    nintendo = nintendo+1
else:
    print("O colaborador 3 digitou um console inexistente e seu voto será desconsiderado")

if voto4 == 1:
    playstation = playstation+1
elif voto4 == 2:
    xbox = xbox+1
elif voto4 == 3:
    nintendo = nintendo+1
else:
    print("O colaborador 4 digitou um console inexistente e seu voto será desconsiderado")

if voto5 == 1:
    playstation = playstation+1
elif voto5 == 2:
    xbox = xbox+1
elif voto5 == 3:
    nintendo = nintendo+1
else:
    print("O colaborador 5 digitou um console inexistente e seu voto será desconsiderado")

if playstation > xbox and playstation > nintendo:
    print("O prêmio escolhido foi o Playstation")
elif xbox > playstation and xbox > nintendo:
    print("O prêmio escolhido foi o XBOX")
elif nintendo > playstation and nintendo > xbox:
    print("O prêmio escolhido foi o Nintendo")
