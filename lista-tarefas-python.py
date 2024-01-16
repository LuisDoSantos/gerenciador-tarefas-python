import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Declaração de variáveis
lista_de_tarefas = []

# Função para adicionar uma nova tarefa
def adicionar_tarefa(descricao):
    nova_tarefa = {"descricao": descricao, "concluida": False}
    lista_de_tarefas.append(nova_tarefa)
    print("Tarefa adicionada com sucesso!")

# Função para exibir a lista de tarefas
def exibir_tarefas():
    if not lista_de_tarefas:
        print("Nenhuma tarefa na lista.")
    else:
        for i, tarefa in enumerate(lista_de_tarefas, 1):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{i}. {tarefa['descricao']} - {status}")

# Função para editar uma tarefa
def editar_tarefa():
    exibir_tarefas()
    try:
        indice = int(input("Digite o número da tarefa que deseja editar: ")) - 1
        if 0 <= indice < len(lista_de_tarefas):
            nova_descricao = input("Digite a nova descrição da tarefa: ")
            lista_de_tarefas[indice]["descricao"] = nova_descricao
            print("Tarefa editada com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Digite um número válido.")

# Função para salvar a lista de tarefas em um arquivo
def salvar_em_arquivo():
    with open("lista_de_tarefas.pkl", "wb") as arquivo:
        pickle.dump(lista_de_tarefas, arquivo)
    print("Lista de tarefas salva em arquivo.")

# Função para autenticar com a API do Google Agenda
def autenticar_google_agenda():
    SCOPES = ["https://www.googleapis.com/auth/calendar.events"]
    creds = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return build("calendar", "v3", credentials=creds)

# Função para adicionar evento à Google Agenda
def adicionar_a_agenda(evento_descricao):
    service = autenticar_google_agenda()
    evento = {"summary": evento_descricao, "description": "Descrição do evento"}

    service.events().insert(
        calendarId="primary",
        body=evento
    ).execute()

    print("Evento adicionado à Google Agenda.")

# Loop principal
while True:
    print("\n--- Lista de Tarefas ---")
    print("1. Adicionar Tarefa")
    print("2. Exibir Tarefas")
    print("3. Editar Tarefa")
    print("4. Salvar em Arquivo")
    print("5. Adicionar à Google Agenda")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        descricao_tarefa = input("Digite a descrição da tarefa: ")
        adicionar_tarefa(descricao_tarefa)
    elif opcao == "2":
        exibir_tarefas()
    elif opcao == "3":
        editar_tarefa()
    elif opcao == "4":
        salvar_em_arquivo()
    elif opcao == "5":
        evento_descricao = input("Digite a descrição do evento: ")
        adicionar_a_agenda(evento_descricao)
    elif opcao == "6":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
