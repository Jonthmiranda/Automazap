#Libraries
import os

Choi = str

while Choi != "Yes" or "Sim":
    #choice language 
    Choi = input("\n\nIf you want in English -> Type Yes\nSe você quer em Português -> Digite Sim\nctrl + C to exit\n\n")
    #English: you chose English
    if Choi == 'Yes':
        print("\nYou chose English\n")
        os.system("python Automazap.py")
    #PortuguÊs: você escolheu portuguÊs
    elif Choi == 'Sim':
        print("Você escolheu em Português\n")
        os.system("python Automazappt-br.py")
