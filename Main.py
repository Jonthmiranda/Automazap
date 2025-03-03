#Libraries
import os

Choi = str

while Choi != "Yes" or "Sim":
    #choice language and you can save yours contacts of whastapp or no, with data scraping, the Whiles is to
    #avoid bugs including the while Choi above 
    Choi = input("\n\nIf you want in English -> Type Yes\nSe você quer em Português -> Digite Sim\nctrl + C to exit\n\n")
    #English: you chose English, now you can save your contacts or no, if no, you go direct to send msg
    if Choi == 'Yes':
        print("\nYou chose English\n")
        SaveContacts = str
        while SaveContacts != "Yes" or "No":
            SaveContacts = input("You want to save yours contacts? Type Yes or No\n")
            if SaveContacts == 'Yes':
                os.system("python RaspaContact.py")
            elif SaveContacts == 'No':
                os.system("python Automazap.py")
    #PortuguÊs: você escolheu portuguÊs, agora você pode salvar seus contatos ou não, se não,
    # você vai direto para enviar suas msg, os whiles são para não ter bugs, incluindo o while Choi acima
    elif Choi == 'Sim':
        print("Você escolheu em Português\n")
        SaveContacts = str
        while SaveContacts != "Sim" or 'Não':
            SaveContacts = input("Você quer salvar seus contatos? digite Sim ou Não\n")
            if SaveContacts == 'Sim':
                os.system("python RaspaContactppt-br.py")
            elif SaveContacts == 'Não':
                os.system("python Automazappt-br.py")
