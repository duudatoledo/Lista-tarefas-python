class Lista_tarefas:
    menu= """
    [1] Adicionar tarefa
    [2] Listar tarefas
    [3] Concluir tarefas
    [4] Sair

=> """
    def __init__(self):
        self.tarefas = []
        pass

    def adc_tarefa(self):
        self.tarefa = (input("Adicionar tarefa:"))
        self.conjunto_tarefa = {"tarefa": self.tarefa, "concluída": False}
        self.tarefas.append(self.conjunto_tarefa)
    
    def listar(self):
        if not self.tarefas:
            print("Nenhuma tarefa")
        else:       
            for i, valor in enumerate(self.tarefas, start=1):
                status = "✓" if valor["concluída"] else "Pendente"
                print(f"{i}- {valor["tarefa"]} [{status}]")

    def concluir(self):
        self.indice = int(input("Qual tarefa deseja concluir?")) - 1
        if 0 <= self.indice < len(self.tarefas): 
            self.tarefas[self.indice]["concluída"] = True
            print("Tarefa concluída")
        else:
            print("Essa tarefa não existe")


    def executar(self):
        while True:
            opcao=(input(self.menu))

            if opcao == "1":
                self.adc_tarefa()

            elif opcao == "2":
                 self.listar()

            elif opcao == "3":
                 self.concluir()
             
            elif opcao== "4":
                 print("Encerrando...")
                 break
             
            else:
                 print("Opção inválida")

conta= Lista_tarefas()
conta.executar()