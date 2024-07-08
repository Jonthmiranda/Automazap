#Libraries
import os

#choice language
Choi = input("\n\nIf you want in English -> Type 1\nSe você quer em Português -> Digite 2\n\n")
if Choi == '1':
    print("You chose in English\n")
    os.system("python Automazap.py")
elif Choi == '2':
    print("Você escolheu em Português\n")
    os.system("python Automazappt-br.py")
else:
    print('error')