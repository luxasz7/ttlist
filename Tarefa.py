from datetime import datetime
import colorama
from colorama import init, Fore, Back, Style

class Tarefa:
    def __init__(self, Lista_Tarefas):
        self.lista_tarefas = Lista_Tarefas

    def new_task(self, comando):
        comando = comando.split()
        task = comando
        task.remove(comando[0])
        execoes = ["add","remove","check","uncheck","exit","done","ls","done","clear","grep","status","edit","exit","help"]

        for i in range(len(task)):
            if task[i] in execoes: 
                print(Fore.RED + f"{task[i]} é um valor invalido.")
            elif task[i] in self.lista_tarefas.tarefas:
                print(Fore.RED + f"{task[i]} já existe na lista impossível adicionar.")
            else:   
                tarefa = task[i]
                date = datetime.now().strftime("%Y-%m-%d %H:%M\n")
                self.lista_tarefas.tarefas[tarefa] = [date,True, ""]
        self.lista_tarefas.dic_tarefas(self.lista_tarefas.tarefas)
        # clear_Terminal()
        # exibir_Lista(tarefas, False)

    def remove_task(self, comando):
        comando = comando.split()
        task = comando
        task.remove(comando[0])

        for i in range(len(task)):
            if task[i] in self.lista_tarefas.tarefas:
                del self.lista_tarefas.tarefas[task[i]]
            elif task[i] == "done":
                continue 
            elif task[i] not in self.lista_tarefas.tarefas:
                print(f"{Fore.RED}{task[i]} não está presente na lista de tarefas. Impossível remover. {Style.RESET_ALL}")
        self.lista_tarefas.dic_tarefas(self.lista_tarefas.tarefas)
        #exibir_Lista(tarefas, False)

    def edit_task(self, t):
        #exibir_Lista(tarefas, True)

        if t == "Null":
                tarefa = input(f"{Back.GREEN}Digite a tarefa que deseja editar:{Style.RESET_ALL} {Fore.GREEN}").lower()
        else:
            tarefa = t
        if tarefa != "done":
            if tarefa in self.lista_tarefas.tarefas:
                new_Tarefa = input(f"{Back.GREEN}Digite as alterações:{Style.RESET_ALL} {Fore.GREEN}").lower()

                while len(new_Tarefa) > 38:
                    new_Tarefa = input(f"{Back.GREEN}A tarefa excede o número de caracteres. Digite as alterações novamente:{Style.RESET_ALL} {Fore.GREEN}").lower()
                if new_Tarefa != "done":
                    date = datetime.now().strftime("%Y-%m-%d %H:%M\n")

                    desc_ask = input(f"{Style.RESET_ALL}{Back.GREEN}Deseja adicionar alguma descrição na tarefa? Y/N{Style.RESET_ALL} {Fore.GREEN}").lower()
                    if desc_ask == 'y':
                        desc = input(f"{Style.RESET_ALL}{Back.GREEN}Digite a descrição:{Style.RESET_ALL} {Fore.GREEN}")
                    else:
                        desc = ""
                        
                    del self.lista_tarefas.tarefas[tarefa]
                    self.lista_tarefas.tarefas[new_Tarefa] = [date,True, desc]

                    self.lista_tarefas.dic_tarefas(self.lista_tarefas.tarefas)
                    #exibir_Lista(tarefas, False)
            else:
                print(f"{Fore.RED}{tarefa} não está presente na lista de tarefas. Impossível Editar.{Style.RESET_ALL}")

    def check_task(self, comando):
        comando = comando.split()
        task = comando
        task.remove(comando[0])
        for i in range(len(task)):
            if task[i] in self.lista_tarefas.tarefas:
                date = self.lista_tarefas.tarefas[task[i]][0]
                desc = self.lista_tarefas.tarefas[task[1][2]]
                self.lista_tarefas.tarefas[task[i]] = [date, False, desc]
                self.lista_tarefas.dic_tarefas(self.lista_tarefas.tarefas)
            else:
                print(f"{Fore.RED}{task[i]} não está presente na lista de tarefas. Impossível marcar como concluido. {Style.RESET_ALL}")
        #exibir_Lista(tarefas, False)

    def uncheck_task(self, comando):
        comando = comando.split()
        task = comando
        task.remove(comando[0])
        for i in range(len(task)):
            if task[i] in self.lista_tarefas.tarefas:
                date = self.lista_tarefas.tarefas[task[i]][0]
                self.lista_tarefas.tarefas[task[i]] = [date, True]
                self.lista_tarefas.dic_tarefas(self.lista_tarefas.tarefas)
            else:
                print(f"{Fore.RED}{task[i]} não está presente na lista de tarefas. Impossível desmarcar como concluido. {Style.RESET_ALL}")
        #exibir_Lista(tarefas,False)