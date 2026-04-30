import json
import os
from pathlib import Path
from datetime import datetime

ROOT_PATH = Path(__file__).parent

class ListaTarefas:
    menu= """
    [1] Adicionar tarefa
    [2] Listar tarefa
    [3] Alterar tarefa
    [4] Excluir tarefa
    [5] Limpar todas as tarefas
    [6] Sair
    [7] Filtrar tarefas
    [8] Estatistica
    => """

    filtros= """
    [1] Prioridade alta
    [2] Prioridade media
    [3] Prioridade baixa
    [4] Concluídas
    [5] Pendentes
    [6] Buscar
    [7] Sair


=> """
    def __init__(self):
        self.tarefas = []
        self.carregar_tarefas()

    def adc_tarefa(self, tarefa, data_entrega):
        tarefa = (input('Adicionar tarefa:')).strip().lower()
        data_entrega = input("Data de entrega (dd/mm/aaaa): ").strip()
        while True:
            self.prioridade = input('Qual o nível de prioridade desta tarefa?(alta, media, baixa): ').strip().lower()
            if self.prioridade in ['alta','media','baixa']:
                    break
            else:
                print('Opção inválida. Tente novamente.')
        print(f'Prioridade selecionada: {self.prioridade}') 
        
        self.conjunto_tarefa = {'tarefa': tarefa, 'concluida': False, 'prioridade': self.prioridade, 'data': datetime.now().strftime('%d/%m/%Y'), 'data_entrega': data_entrega}
        self.tarefas.append(self.conjunto_tarefa)
        self.salvar_arquivo()    
    
    def listar(self):
        
        if not self.tarefas:
            print('Nenhuma tarefa')
        else:
            self.ordem_prioridades() 
            print(f"{'Nº':<3} | {'TAREFA':<20} | {'STATUS':<10} | {'PRIORIDADE':<10} | {'DATA':<10}") 
            print('-' * 70)      
            for i, valor in enumerate(self.tarefas, start=1):
                status = 'Concluída' if valor['concluida'] else 'Pendente'
                print(f"{i:<3} | {valor['tarefa'][:20]:<20} | {status:<10} | {valor['prioridade']:<10} | {valor['data']:<10}")

    def ordem_prioridades(self,conversao_prioridade):
        conversao_prioridade = {'alta': 1, 'media': 2, 'baixa': 3}
        tipo = input("""Como deseja ordenar?
            [1] Prioridade
            [2] Data de entrega

            => """)
        
        if tipo == '1':
            self.tarefas.sort(key=lambda valor: conversao_prioridade[valor['prioridade']])
       
        elif tipo == '2':
            self.tarefas.sort(
            key=lambda t: datetime.strptime(t['data_entrega'], '%d/%m/%Y')
        )
        else:
            print("Opção inválida. Tente novamente")


    def alterar_sistema(self, indice):

        try:

            indice = int(input('Qual tarefa deseja alterar?')) - 1
        
            if 0 <= indice < len(self.tarefas): 
                self.tarefas[indice]['concluida'] = not self.tarefas[indice]['concluida'] 
            
                if self.tarefas[indice]['concluida']:
                    print('Tarefa concluída ✔')
            
                else:
                    print('Tarefa alterada')
            else:
                print('Essa tarefa não existe')

            self.salvar_arquivo()

        except:
            print("Opção inválida. Digite apenas números.")
            return

    def excluir_tarefa(self, indice):

        try:
  
            indice = int(input('Qual tarefa deseja excluir?')) - 1
            if 0 <= indice < len(self.tarefas): 
                self.tarefas.pop(indice)
                print('Tarefa excluida')
            else:
                print('Essa tarefa não existe')
            self.salvar_arquivo()

        except:
            print("Opção inválida. Digite apenas números.")

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
            opcao= input(self.menu)

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

            elif opcao== '7':
                self.filtrar_tarefas()

            elif opcao =='8':
                self.estatisticas()
             
            else:
                print('Opção inválida')

    def salvar_arquivo(self):

        with open(ROOT_PATH / 'tarefas.json', 'w') as arquivo:
            json.dump(self.tarefas, arquivo, indent=4)
            print('Salvando...\nSalvo.', os.getcwd())
    
    def carregar_tarefas(self):

        try:
            with open(ROOT_PATH / 'tarefas.json', 'r') as arquivo:
                self.dados = json.load(arquivo)
                self.tarefas = self.dados
                print('CARREGANDO...')

        except Exception as e:
            print("ERRO AO CARREGAR:", e)
            self.tarefas = []

    def filtrar_tarefas(self):
        while True:
            filtro=input(f"Como deseja filtrar as tarefas?: {(self.filtros)}" )

            if filtro == '1':
                print(f"{'Nº':<3} | {'TAREFA':<20} | {'STATUS':<10} | {'PRIORIDADE':<10}") 
                print('-' * 55) 
                for i, valor in enumerate(self.tarefas, start=1):
                    if valor['prioridade'] == 'alta':
                        status = 'Concluída' if valor['concluida'] else 'Pendente'
                        print(f"{i:<3} | {valor['tarefa'][:20]:<20} | {status:<10} | {valor['prioridade']:<10}")

            elif filtro == '2':
                print(f"{'Nº':<3} | {'TAREFA':<20} | {'STATUS':<10} | {'PRIORIDADE':<10}") 
                print('-' * 55) 
                for i, valor in enumerate(self.tarefas, start=1):
                    if valor['prioridade'] == 'media':
                        status = 'Concluída' if valor['concluida'] else 'Pendente'
                        print(f"{i:<3} | {valor['tarefa'][:20]:<20} | {status:<10} | {valor['prioridade']:<10}")

            elif filtro == '3':
                print(f"{'Nº':<3} | {'TAREFA':<20} | {'STATUS':<10} | {'PRIORIDADE':<10}") 
                print('-' * 55) 
                for i, valor in enumerate(self.tarefas, start=1):
                    if valor['prioridade'] == 'baixa':
                        status = 'Concluída' if valor['concluida'] else 'Pendente'
                        print(f"{i:<3} | {valor['tarefa'][:20]:<20} | {status:<10} | {valor['prioridade']:<10}")

            elif filtro == '4': 
                print(f"{'Nº':<3} | {'TAREFA':<20} | {'STATUS':<10} | {'PRIORIDADE':<10}") 
                print('-' * 55) 
                for i,valor in enumerate(self.tarefas, start=1):
                    if valor['concluida'] == True:
                        status = 'Concluída' if valor['concluida'] else 'Pendente'
                        print(f"{i:<3} | {valor['tarefa'][:20]:<20} | {status:<10} | {valor['prioridade']:<10}")

            elif filtro == '5':
                print(f"{'Nº':<3} | {'TAREFA':<20} | {'STATUS':<10} | {'PRIORIDADE':<10}") 
                print('-' * 55) 
                for i,valor in enumerate(self.tarefas, start=1):
                    if valor['concluida'] == False:
                        status = 'Concluída' if valor['concluida'] else 'Pendente'
                        print(f"{i:<3} | {valor['tarefa'][:20]:<20} | {status:<10} | {valor['prioridade']:<10}")
            
            elif filtro == '6':
                buscar = input("O que quer buscar?").strip().lower()
                print(f"{'Nº':<3} | {'TAREFA':<20} | {'STATUS':<10} | {'PRIORIDADE':<10}") 
                print('-' * 55) 
                self.encontrou = False
                for i,tarefa in enumerate(self.tarefas, start=1):
                    if buscar in tarefa['tarefa'].lower():
                        self.encontrou = True
                        status = 'Concluída' if tarefa['concluida'] else 'Pendente'
                        print(f"{i:<3} | {tarefa['tarefa'][:20]:<20} | {status:<10} | {tarefa['prioridade']:<10}")
                if self.encontrou == False:
                    print('Nenhuma tarefa encontrada.')

            elif filtro== '7':
                print('Encerrando...')
                break

    def estatisticas(self):
        con = 0
        pen = 0
        al = 0
        bai = 0
        med = 0
        for valor in self.tarefas:
            if valor['concluida']:
                con += 1
            else:
                pen +=1

            if valor['prioridade'] == 'alta':
                al += 1

            if valor['prioridade'] == 'media':
                med += 1
            
            if valor['prioridade'] == 'baixa':
                bai += 1

        porcentagem = (con / len(self.tarefas)) * 100 if self.tarefas else 0

        print(f"""======= ESTATÍSTICAS =======
        Total:        {len(self.tarefas)}  
        Concluídas:   {con} ({porcentagem:.1f}%)
        Pendentes:    {pen}

        ALTA:         {al}
        MEDIA:        {med}
        BAIXA:        {bai}
        """)


conta = ListaTarefas()
conta.executar()
