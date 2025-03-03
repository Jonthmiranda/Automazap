Português | [English](https://github.com/Jonthmiranda/Automazap/blob/main/README.md)

# Automazap 1.4

## Descrição

Sistema de automação em Python para envio de cardápios e descrição para contatos no Whatsapp Web, e raspagem de dados para salvamento de contatos em .xlsx

bibliotecas: Selenium, Pyautogui, Pandas e urllib.

## Funcionalidades Principais

- Envio Automático de Cardápios: O sistema lê os arquivos de cardápios (PDF, JPG, PNG, etc.) de um diretório específico e os envia automaticamente para os clientes.


- Mensagem Personalizada: Permite o envio de uma mensagem personalizada junto com os cardápios para todos os números listados no arquivo `Contatos.xlsx`.

- Raspagem de dados do whastapp para salvamento de contatos em .xlsx


## Benefícios

- Economia de Tempo: Automatiza o processo de envio de cardápios, permitindo que os funcionários se concentrem em outras tarefas.
- Facilidade de Uso: Basta organizar os arquivos de cardápios no diretório e o sistema cuida do resto.
- Sem perda de tempo salvando contatos em uma planilha excell.

## Requisitos

- Python instalado
- Bibliotecas Selenium , Pandas, PyautoGUI
- Acesso à internet
- Google Chrome
- WhatsApp no smartphone para acesso ao WhatsApp Web

## Instalação

```bash
git clone https://github.com/Jonthmiranda/Automazap
```

## Uso
1º Os cardapios que serão enviados para os clientes deveram estar na pasta "cardapio", numerada para ordem que será enviado ex: 1 -> primeiro, 2 -> segundo etc...

2º Os contatos de para quem será enviado está no Contatos.xlsx

Inicie Main.py usando uma IDE Python ou CMD;

Você pode escolher a linguagem entre Português e Inglês e se quer salvar contatos ou mandar os cardapios diretamente

Depois de você escolher a linguagem e escrever a mensagem, você não precisa mexer no computador, lembre-se, linha 21 e 22 do Automazappt-br.py, precisa estar habilitado para rodar corretamente em uma IDE ou CMD, ao criar .exe essas linhas precisam estar desativadas e não deverá ter nada aberto além da IDE

## Melhorias

1.1 -> adicionada versão em inglês;

1.2 -> Corrigido erro quando o WhatsApp web apresenta erro no número do telefone;

1.3 -> Tempo melhorado e correção de diretório de menu

1.4 -> Correções de bugs e adicionado raspagem de dados para salvar contatos