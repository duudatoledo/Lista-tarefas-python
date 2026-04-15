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
        self.tarefas.append(self.tarefa)
    
    def listar(self):
        if not self.tarefas:
            print("Nenhuma tarefa")
        else:
            for self.tarefa in self.tarefas:
                print(self.tarefa)

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