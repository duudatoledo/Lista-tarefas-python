import json

class Lista_tarefas:
    menu= """
    [1] Adicionar tarefa
    [2] Listar tarefa
    [3] Alterar tarefa
    [4] Excluir tarefa
    [5] Sair

=> """
    def __init__(self):

        self.tarefas = []
        self.carregar_tarefas()
        pass

    def adc_tarefa(self):

        self.tarefa = (input("Adicionar tarefa:"))
        self.conjunto_tarefa = {"tarefa": self.tarefa, "concluida": False}
        self.tarefas.append(self.conjunto_tarefa)
        self.salvar_arquivo()    
    
    def listar(self):

        if not self.tarefas:
            print("Nenhuma tarefa")
        else:       
            for i, valor in enumerate(self.tarefas, start=1):
                status = "✓" if valor["concluida"] else "Pendente"
                print(f"{i}- {valor["tarefa"]} [{status}]")

    def alterar_sistema(self):

        self.indice = int(input("Qual tarefa deseja alterar?")) - 1
        
        if 0 <= self.indice < len(self.tarefas): 
            self.tarefas[self.indice]["concluida"] = not self.tarefas[self.indice]["concluida"] 
            
            if self.tarefas[self.indice]["concluida"]:
                 print("Tarefa concluída ✔")
            
            else:
                print("Tarefa alterada")
        else:
            print("Essa tarefa não existe")

    def excluir_tarefa(self):

        self.indice = int(input("Qual tarefa deseja excluir?")) - 1
        if 0 <= self.indice < len(self.tarefas): 
            self.tarefas.pop(self.indice)
            print("Tarefa excluida")
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
                self.alterar_sistema()

            elif opcao == "4":
                self.excluir_tarefa()

            elif opcao== "5":
                 print("Encerrando...")
                 break
             
            else:
                 print("Opção inválida")

    def salvar_arquivo(self):

        with open("tarefas.json", "w") as arquivo:
            json.dump(self.tarefas, arquivo, indent=4)
            print("Salvando..." 
            "\nSalvo.")
    
    def carregar_tarefas(self):

        try:
            with open("tarefas.json", "r") as arquivo:
                self.dados = json.load(arquivo)
                self.tarefas = self.dados
                print("CARREGANDO...", self.tarefas)
        except:
            self.tarefas = []

conta= Lista_tarefas()
conta.executar()