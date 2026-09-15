# CRUD TASKFLOW - Gerenciador de Estudo e Tarefas

tarefas = []


# CREATE - Cadastrar tarefa
def cadastrar_tarefa():
    print("\n===== CADASTRAR TAREFA =====")

    # RN02 - Título com no mínimo 3 caracteres
    while True:
        titulo = input("Título da tarefa: ").strip()

        if len(titulo) >= 3:
            break

        print("O título deve ter no mínimo 3 caracteres.")

    materia = input("Matéria/Assunto: ").strip()

    # RN01 - Prioridade entre 1 e 3
    while True:
        prioridade = int(input("Prioridade (1-Baixa, 2-Média, 3-Alta): "))

        if prioridade >= 1 and prioridade <= 3:
            break

        print("A prioridade deve ser 1, 2 ou 3.")

    # Prazo em dias
    while True:
        prazo = int(input("Dias restantes para o prazo: "))

        if prazo >= 0:
            break

        print("O prazo não pode ser negativo.")

    # RN03 - Horas maiores que zero
    while True:
        horas = float(input("Horas estimadas: "))

        if horas > 0:
            break

        print("As horas devem ser maiores que zero.")

    descricao = input("Descrição: ").strip()

    # RN04 - Calcula a urgência automaticamente
    if prazo <= 2:
        urgencia = "Urgente"
    else:
        urgencia = "No Prazo"

    tarefa = {
        "titulo": titulo,
        "materia": materia,
        "prioridade": prioridade,
        "prazo": prazo,
        "horas": horas,
        "descricao": descricao,
        "urgencia": urgencia,
        "status": "Pendente"
    }

    tarefas.append(tarefa)

    print("\nTarefa cadastrada com sucesso!")
    print("Urgência:", urgencia)


# READ - Listar tarefas
def listar_tarefas():
    print("\n===== LISTA DE TAREFAS =====")

    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, tarefa in enumerate(tarefas):
        print("\n-----------------------------")
        print("ID:", i + 1)
        print("Título:", tarefa["titulo"])
        print("Matéria:", tarefa["materia"])
        print("Prioridade:", tarefa["prioridade"])
        print("Prazo:", tarefa["prazo"], "dias")
        print("Horas estimadas:", tarefa["horas"])
        print("Descrição:", tarefa["descricao"])
        print("Urgência:", tarefa["urgencia"])
        print("Status:", tarefa["status"])


# UPDATE - Atualizar tarefa
def atualizar_tarefa():
    listar_tarefas()

    if len(tarefas) == 0:
        return

    id_tarefa = int(input("\nDigite o ID da tarefa que deseja atualizar: "))

    if id_tarefa < 1 or id_tarefa > len(tarefas):
        print("ID inválido.")
        return

    tarefa = tarefas[id_tarefa - 1]

    print("\n===== ATUALIZAR TAREFA =====")

    titulo = input("Novo título: ").strip()

    if len(titulo) >= 3:
        tarefa["titulo"] = titulo
    else:
        print("Título não alterado. Deve ter no mínimo 3 caracteres.")

    materia = input("Nova matéria: ").strip()

    if materia != "":
        tarefa["materia"] = materia

    prioridade = int(input("Nova prioridade (1-Baixa, 2-Média, 3-Alta): "))

    if prioridade >= 1 and prioridade <= 3:
        tarefa["prioridade"] = prioridade
    else:
        print("Prioridade inválida. Valor não alterado.")

    prazo = int(input("Novo prazo em dias: "))

    if prazo >= 0:
        tarefa["prazo"] = prazo
    else:
        print("Prazo inválido. Valor não alterado.")

    horas = float(input("Novas horas estimadas: "))

    if horas > 0:
        tarefa["horas"] = horas
    else:
        print("Horas inválidas. Valor não alterado.")

    descricao = input("Nova descrição: ").strip()

    if descricao != "":
        tarefa["descricao"] = descricao

    print("\nStatus atual:", tarefa["status"])
    print("1 - Pendente")
    print("2 - Concluída")
    print("3 - Cancelada")

    opcao_status = input("Escolha o novo status: ")

    if opcao_status == "1":
        tarefa["status"] = "Pendente"
    elif opcao_status == "2":
        tarefa["status"] = "Concluída"
    elif opcao_status == "3":
        tarefa["status"] = "Cancelada"
    else:
        print("Status inválido. Status não alterado.")

    # RN04 - Atualiza a urgência depois da alteração do prazo
    if tarefa["prazo"] <= 2:
        tarefa["urgencia"] = "Urgente"
    else:
        tarefa["urgencia"] = "No Prazo"

    print("\nTarefa atualizada com sucesso!")


# DELETE - Remover tarefa
def remover_tarefa():
    listar_tarefas()

    if len(tarefas) == 0:
        return

    id_tarefa = int(input("\nDigite o ID da tarefa que deseja remover: "))

    if id_tarefa < 1 or id_tarefa > len(tarefas):
        print("ID inválido.")
        return

    tarefa = tarefas[id_tarefa - 1]

    # Só permite remover tarefas concluídas ou canceladas
    if tarefa["status"] != "Concluída" and tarefa["status"] != "Cancelada":
        print("\nA tarefa precisa estar Concluída ou Cancelada para ser removida.")
        return

    tarefas.pop(id_tarefa - 1)

    print("\nTarefa removida com sucesso!")


# MENU PRINCIPAL
def menu():
    while True:
        print("\n================================")
        print("          CRUD TASKFLOW")
        print("   Gerenciador de Estudos")
        print("================================")
        print("1 - Cadastrar tarefa")
        print("2 - Listar tarefas")
        print("3 - Atualizar tarefa")
        print("4 - Remover tarefa")
        print("5 - Sair")
        print("================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_tarefa()

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            atualizar_tarefa()

        elif opcao == "4":
            remover_tarefa()

        elif opcao == "5":
            print("\nPrograma encerrado.")
            break

        else:
            print("\nOpção inválida. Escolha de 1 a 5.")


# Inicia o programa
menu()
