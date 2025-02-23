MIN_NOME_TAREFA = 2

# lista todas as tarefas registradas
def listar_tarefas(tarefas):
  for tarefa in tarefas:
    print(f"tarefa {tarefa[0]}: {tarefa[1]}; descrição: {tarefa[2]}; status: {tarefa[3]}; prazo final: {tarefa[4]}.")

tarefas = [[1, "Estudar inglês", "Utilizar o livro Keep Talking Three", "Pendente", "2025/02/15", "Média"], [2, "Comprar teclado novo", "Comparar os preços", "Em execução", "2025/05/01"]]

# valida o tamanho mínimo do nome
def validar_nome():
  while (True):
    nomeTarefa = input("Digite o nome da tarefa: ")
    if len(nomeTarefa) < MIN_NOME_TAREFA:
      print("Digite um nome válido!")
    else:
      break
  return nomeTarefa

# adiciona uma nova tarefa
def incluir_tarefa(tarefas):
  novoId = len(tarefas) + 1
  nomeTarefa = validar_nome()
  while nomeTarefa.lower() != 'fim':
    descricao = input("Digite uma descrição para a tarefa: ")
    status = input("Digite a opção desejada (Pendente, Em andamento, Concluída): ")
    prazo = input("Digite o prazo final para a conclusão da tarefa: ")
    urgencia = input("Digite 'baixa', 'média' ou 'alta' para urgência da tarefa: ")
    tarefa = [novoId, nomeTarefa, descricao, status, prazo, urgencia]
    tarefas.append(tarefa)
    novoId += 1
    nomeTarefa = input("Digite o nome da tarefa ou 'fim' para finalizar: ")
  return tarefas

# altera o status de uma tarefa como concluída
def marcar_como_concluida(tarefaId):
  print("Segue a lista atualizada de tarefas:")
  listar_tarefas(tarefas)
  tarefaId = int(input("Digite o número da tarefa que deseja concluir: "))
  for tarefa in tarefas:
    if tarefa[0] == tarefaId:
      tarefa[3] = "Concluída"
      print(f"Tarefa {tarefaId} marcada como Concluída!")
      break
    else:
      print("Tarefa não encontrada.")

# remove uma tarefa específica da lista
def remover_tarefa(tarefas):
  print("Segue a lista atualizada de tarefas:")
  listar_tarefas(tarefas)
  tarefaId = int(input("Digite o número da tarefa que deseja excluir: "))
  tarefaEncontrada = False
  for tarefa in tarefas:
    if tarefa[0] == tarefaId:
      tarefas.remove(tarefa)
      print(f"A tarefa {tarefaId} foi removida!")
      tarefaEncontrada = True
      break
    
  if not tarefaEncontrada:
    print("Tarefa não encontrada.")

# menu interativo
def menu():
  """Função de menu interativo"""
  while True:
    print("\n****************************************")
    print("Menu:")
    print("1. Listar tarefas")
    print("2. Incluir tarefa")
    print("3. Marcar como concluída")
    print("4. Excluir tarefa")
    print("0. Sair")
    print("****************************************")
    opcao = input("Escolha uma opção, digitando apenas o número da opção escolhida: ")
    if opcao == '1':
      listar_tarefas(tarefas)
    elif opcao == '2':
      incluir_tarefa(tarefas)
    elif opcao == '3':
      marcar_como_concluida(tarefas)
    elif opcao == '4':
      remover_tarefa(tarefas)
    elif opcao == '0':
      print("Saindo...")
      break
    else:
      print("Ops! Opção inválida. Tente novamente.")

# executa o menu interativo
menu()