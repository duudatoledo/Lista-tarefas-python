import json
import os
from pathlib import Path

ROOT_PATH = Path(__file__).parent

class Lista_tarefas:
    menu= """
    [1] Adicionar tarefa
    [2] Listar tarefa
    [3] Alterar tarefa
    [4] Excluir tarefa
    [5] Limpar todas as tarefas
    [6] Sair

=> """
    def __init__(self):

        self.tarefas = []
        self.carregar_tarefas()
        pass

    def adc_tarefa(self):

        self.tarefa = (input('Adicionar tarefa:'))

        while True:
            self.prioridade = input('Qual o nível de prioridade desta tarefa?(alta, media, baixa): ').strip().lower()
           
            if self.prioridade in ['ALTA','media','baixa']:
                    break
            else:
                print('Opção inválida. Tente novamente.')
        print(f'Prioridade selecionada: {self.prioridade}') 
        
        self.conjunto_tarefa = {'tarefa': self.tarefa, 'concluida': False, 'prioridade': self.prioridade}
        self.tarefas.append(self.conjunto_tarefa)
    
        self.salvar_arquivo()    
    
    def listar(self):

        if not self.tarefas:
            print('Nenhuma tarefa')
        else:
            self.ordem_prioridades() 
            print(f"{'Nº':<3} | {'TAREFA':<20} | {'STATUS':<10} | {'PRIORIDADE':<10}" ('-' * 55))      
            for i, valor in enumerate(self.tarefas, start=1):
                status = 'Concluída' if valor['concluida'] else 'Pendente'
                print(f'{i:<3} | {valor['tarefa'][:20]:<20} | {status:<10} | {valor['prioridade']:<10}')

    def ordem_prioridades(self):
        self.conversao_prioridade = {'ALTA': 1, 'media': 2, 'baixa': 3}
        self.tarefas.sort(key=lambda valor: self.conversao_prioridade[valor['prioridade']])
        
    def alterar_sistema(self):

        self.indice = int(input('Qual tarefa deseja alterar?')) - 1
        
        if 0 <= self.indice < len(self.tarefas): 
            self.tarefas[self.indice]['concluida'] = not self.tarefas[self.indice]['concluida'] 
            
            if self.tarefas[self.indice]['concluida']:
                 print('Tarefa concluída ✔')
            
            else:
                print('Tarefa alterada')
        else:
            print('Essa tarefa não existe')
        self.salvar_arquivo()

    def excluir_tarefa(self):

        self.indice = int(input('Qual tarefa deseja excluir?')) - 1
        if 0 <= self.indice < len(self.tarefas): 
            self.tarefas.pop(self.indice)
            print('Tarefa excluida')
        else:
            print('Essa tarefa não existe')
        self.salvar_arquivo()

    def limpar_tarefas(self):
        self.apagar = input('Tem certeza?(n/s):').lower().strip()
        
        if self.apagar == "s" or self.apagar == "sim":
            self.tarefas.clear()
            self.salvar_arquivo()
            print('Tarefas excluidas com sucesso!')
        
        elif self.apagar == "n" or self.apagar == "não" or self.apagar == "nao":
            print("Ação cancelada.")
        else:
            print("Resposta inválida.")    

    def executar(self):

        while True:
            opcao=(input(self.menu))

            if opcao == '1':
                self.adc_tarefa()

            elif opcao == '2':
                self.listar()

            elif opcao == '3':
                self.alterar_sistema()

            elif opcao == '4':
                self.excluir_tarefa()

            elif opcao == '5':
                self.limpar_tarefas()

            elif opcao== '6':
                print('Encerrando...')
                break
             
            else:
                print('Opção inválida')

    def salvar_arquivo(self):

        with open(ROOT_PATH / 'tarefas.json', 'w') as arquivo:
            json.dump(self.tarefas, arquivo, indent=4)
            print('Salvando...' 
            '\nSalvo.', os.getcwd())
    
    def carregar_tarefas(self):

        try:
            with open('tarefas.json', 'r') as arquivo:
                self.dados = json.load(arquivo)
                self.tarefas = self.dados
                print('CARREGANDO...')
        except:
            self.tarefas = []

conta= Lista_tarefas()
conta.executar()