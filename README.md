# Projeto: Gerenciador de Tarefas em Python

## Descrição

Este projeto consiste em um aplicativo de linha de comando (CLI) em Python para gerenciar uma lista de tarefas. Ele oferece funcionalidades como adicionar tarefas, exibir a lista, editar tarefas, salvar a lista em um arquivo e adicionar eventos à Google Agenda.

## Funcionalidades

1. **Adicionar Tarefa:**
   - Permite ao usuário adicionar novas tarefas à lista.

2. **Exibir Tarefas:**
   - Mostra a lista atual de tarefas, indicando se cada uma está concluída ou pendente.

3. **Editar Tarefa:**
   - Permite ao usuário editar uma tarefa existente, alterando sua descrição.

4. **Salvar em Arquivo:**
   - Salva a lista de tarefas em um arquivo `lista_de_tarefas.pkl` usando o módulo `pickle`.

5. **Adicionar à Google Agenda:**
   - Adiciona eventos à Google Agenda utilizando a API do Google Calendar. Os eventos são definidos com base na descrição da tarefa.

## Tecnologias Utilizadas

- **Python 3:** Linguagem de programação principal.
- **Pickle:** Módulo Python para serialização e desserialização de objetos Python.
- **Google API Python Client:** Biblioteca utilizada para interagir com a API do Google Agenda.
- **OAuth 2.0:** Utilizado para autenticação com a API do Google Agenda.

## Configuração e Uso

1. **Instale as Dependências:**
   - Execute `pip install -r requirements.txt` para instalar as bibliotecas necessárias.

2. **Configure as Credenciais da API do Google:**
   - Crie um projeto no [Google Developers Console](https://console.developers.google.com/) e habilite a API do Google Calendar.
   - Baixe as credenciais JSON e renomeie o arquivo para `credentials.json`.
   - Execute o script para autenticar e obter o token para acesso à Google Agenda.

3. **Execute o Projeto:**
   - Execute o script principal `gerenciador_tarefas.py` para começar a utilizar o aplicativo.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, propor melhorias ou enviar pull requests.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
