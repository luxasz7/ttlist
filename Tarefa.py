from datetime import datetime
import colorama
from colorama import init, Fore, Back, Style
from Commands import Commands

class Tarefa(Commands):
    def __init__(self, Lista_Tarefas):
        self.lista_tarefas = Lista_Tarefas

    def new_task(self, comando):
        #comando = comando.split()
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
        self.clear()
        self.ls(False)
        # clear_Terminal()
        # exibir_Lista(tarefas, False)

    def new_task_w(self):
        self.ls(False)
        tarefa = ""

        while tarefa != "done":
            tarefa = input(f"{Style.RESET_ALL}{Back.GREEN}Digite a tarefa:{Style.RESET_ALL}{Fore.GREEN}").lower()
            self.ls(False)

            if tarefa == "done":
                break

            tarefa = tarefa.replace(" ","_")    

            self.new_task(["add",tarefa])

            if tarefa in self.lista_tarefas.tarefas: 

                desc_ask = input(f"{Style.RESET_ALL}{Back.GREEN}Deseja adicionar alguma descrição na tarefa? Y/N{Style.RESET_ALL}  {Fore.GREEN}").lower()

                if desc_ask == 'y':
                    desc = input(f"{Style.RESET_ALL}{Back.GREEN}Digite a descrição:{Style.RESET_ALL} {Fore.GREEN}")
                    self.lista_tarefas.tarefas[tarefa][2] = desc
                    self.new_task(["add",tarefa])

                    self.ls(False)
                else:
                    self.ls(False)
                    continue

    def remove_task(self, comando):
        #comando = comando.split()
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
        self.clear()
        self.ls(False)
        #exibir_Lista(tarefas, False)

    def remove_task_w(self):
        self.ls(False)
        tarefa = ""
        self.ls(False)
        while tarefa != "done":
            tarefa = input(f"{Back.RED}{Fore.WHITE}Digite a tarefa que deseja remover:{Style.RESET_ALL} {Fore.RED}").lower()
            self.remove_task(["remove",tarefa])

    def edit_task(self, t):
        self.ls(False)

        if t == "Null":
                tarefa = input(f"{Style.RESET_ALL}{Back.GREEN}Digite a tarefa que deseja editar:{Style.RESET_ALL} {Fore.GREEN}").lower()
        else:
            tarefa = t
        if tarefa != "done":
            if tarefa in self.lista_tarefas.tarefas:
                new_Tarefa = input(f"{Style.RESET_ALL}{Back.GREEN}Digite as alterações:{Style.RESET_ALL} {Fore.GREEN}").lower()
                new_Tarefa = new_Tarefa.replace(" ", "_")
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
                    self.lista_tarefas.tarefas[new_Tarefa] = [date, True, desc]

                    self.lista_tarefas.dic_tarefas(self.lista_tarefas.tarefas)
                    self.ls(False)
            else:
                print(f"{Fore.RED}{tarefa} não está presente na lista de tarefas. Impossível Editar.{Style.RESET_ALL}")
            self.clear()
            self.ls(False)

    def check_task(self, comando):
        #comando = comando.split()
        task = comando
        task.remove(comando[0])
        for i in range(len(task)):
            if task[i] in self.lista_tarefas.tarefas:
                date = self.lista_tarefas.tarefas[task[i]][0]
                desc = self.lista_tarefas.tarefas[task[i]][0]
                self.lista_tarefas.tarefas[task[i]] = [date, False, desc]
                self.lista_tarefas.dic_tarefas(self.lista_tarefas.tarefas)
            else:
                print(f"{Fore.RED}{task[i]} não está presente na lista de tarefas. Impossível marcar como concluido. {Style.RESET_ALL}")
        #exibir_Lista(tarefas, False)
        self.clear()
        self.ls(False)

    def check_task_w(self):
        tarefa = ""
        while tarefa != "done":
            tarefa = input(f"{Style.RESET_ALL}{Back.GREEN}Digite a tarefa que deseja marcar como concluida:{Style.RESET_ALL} {Fore.GREEN}").lower()
            if tarefa == "done":
                break
            self.check_task(["check",tarefa])
        self.ls(False) 

    def uncheck_task(self, comando):
        #comando = comando.split()
        task = comando
        task.remove(comando[0])
        for i in range(len(task)):
            if task[i] in self.lista_tarefas.tarefas:
                date = self.lista_tarefas.tarefas[task[i]][0]
                self.lista_tarefas.tarefas[task[i]] = [date, True, ""]
                self.lista_tarefas.dic_tarefas(self.lista_tarefas.tarefas)
            else:
                print(f"{Fore.RED}{task[i]} não está presente na lista de tarefas. Impossível desmarcar como concluido. {Style.RESET_ALL}")
        #exibir_Lista(tarefas,False)
        self.clear()
        self.ls(False)

    def uncheck_task_w(self):
        tarefa = ""
        while tarefa != "done":
            tarefa = input(f"{Style.RESET_ALL}{Back.GREEN}Digite a tarefa que deseja desmarcar como concluida:{Style.RESET_ALL} {Fore.GREEN}").lower()
            if tarefa == "done":
                break
            self.uncheck_task(["check",tarefa])
        self.clear()
        self.ls(False)