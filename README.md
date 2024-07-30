[Português](https://github.com/Jonthmiranda/Automazap/blob/main/README%20pt-br.md) | English

# Automazap 1.3

 ## Description

 Automation system in Python for sending menus and descriptions to contacts on Whatsapp Web.

 libraries: Selenium, Pyautogui, Pandas and urllib.

 ## Main Features

 - Automatic Menu Sending: The system reads menu files (PDF, JPG, PNG, etc.) from a specific directory and automatically sends them to customers.


 - Personalized Message: Allows sending a personalized message along with the menus to all numbers listed in the `Contacts.xlsx` file.


 ## Benefits

 - Time Saving: Automates the menu sending process, allowing employees to focus on other tasks.
 - Ease of Use: Simply organize the menu files in the directory and the system takes care of the rest.


 ## Requirements

 - Python installed
 - Selenium, Pandas, PyautoGUI Libraries
 - Internet access
 - Google Chrome
 - WhatsApp on your smartphone to access WhatsApp Web

 ## Installation

 ```bash
 git clone https://github.com/Jonthmiranda/Automazap
 ```

 ## Usage
 1st The menus that will be sent to customers must be in the "menu" folder, numbered in the order in which they will be sent e.g.: 1 -> first, 2 -> second, etc...

 2nd The contact details to whom it will be sent are in Contacts.xlsx

 Launch Main.py using a Python IDE or CMD;

 You can choose the language between Portuguese and English

 After you choose the language and write the message, you don't need to use the computer, remember, line 21 and 22 of Automazappt-br.py, it needs to be enabled to run correctly in an IDE or CMD, when creating .exe these lines must be disabled and there must be nothing open other than the IDE

## version

1.1 -> added English version;

1.2 -> Fixed error when WhatsApp web has an error in the phone number;

1.3 -> Improved timing and menu directory correction
