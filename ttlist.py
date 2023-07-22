from datetime import datetime
import colorama
from colorama import init, Fore, Back, Style
colorama.init(autoreset=True)
import json
import subprocess
import platform

with open('arquivo.json','r') as arquivo:
    arquivo = json.load(arquivo)

c = ""
tarefas = arquivo

def adicionar_Tarefa(tarefas):    
    with open('arquivo.json','w') as arquivo:
        json.dump(tarefas, arquivo)

def exec_Comando(c):
    comando = c.split()

    match comando[0]:
        case "add":
            for i in range(1,len(comando)):
                if len(comando[i]) > 35:
                    print(f"{comando[i]} excede o número de caracteres.")
                    comando.remove(comando[i])              
            if len(comando) == 1:
                    add_Tarefa_W()
            elif len(comando) > 0:
                    add_Tarefa(comando)
        case "remove":
            if len(comando) == 1:
                remove_Tarefa_W()
            else:
                remove_Tarefa(comando)
        case "check":
                if len(comando) == 1:
                    checked_Tarefa_W(comando)
                elif len(comando) > 0:
                    checked_Tarefa(comando)
        case "uncheck":
            if len(comando) == 1:
                unchecked_Tarefa_W(comando)
            elif len(comando) > 0:
                unchecked_Tarefa(comando)
        case "help":
            print(f"{Back.LIGHTMAGENTA_EX}--------------------------------------{Style.RESET_ALL}\n{Back.LIGHTBLUE_EX}add - Adiciona uma nova terafa{Style.RESET_ALL}\n{Back.LIGHTBLUE_EX}remove - Remove um tarefa{Style.RESET_ALL}\n{Back.LIGHTBLUE_EX}check - Marca uma tarefa com concluída{Style.RESET_ALL}\n{Back.LIGHTBLUE_EX}ls - Lista as terafas{Style.RESET_ALL}\n{Back.LIGHTBLUE_EX}ls -h - Lista as tarefas exibindo seu horário de criação{Style.RESET_ALL}\n{Back.LIGHTMAGENTA_EX}--------------------------------------{Style.RESET_ALL}")
        case "exit":
            print(f"{Back.LIGHTMAGENTA_EX}Saindo...")
        case "ls":
            if len(comando) == 1:
                exibir_Lista(tarefas,False)
            elif len(comando) == 2 and comando[1] == "-h":
                exibir_Lista(tarefas,True)
            else:
                print(f"{Fore.RED}Comando invalido.")
        case "clear":
            clear_Terminal()
        case "edit":
            if len(comando) == 1:
                editar_Tarefa(tarefas, "Null")
            elif len(comando) == 2:
                editar_Tarefa(tarefas,comando[1])
            elif len(comando) > 2:
                print(f"{Fore.RED}Comando invalido. Você só pode editar um item por vez.")
        case "status":
            if len(comando) == 1:
                status(False)
            elif len(comando) > 1 and comando[1] == 'p':
                status(True)
            elif len(comando) > 1 and comando[1] != 'p':
                print(Fore.RED + "Comando inválido, digite \"help\" para ver a lista de comandos\n")
        case "grep":
            if len(comando) == 2:
                grep(comando[1])
            elif len(comando) > 2:
                print(Fore.RED + "Comando inválido, digite \"help\" para ver a lista de comandos\n")
        case other:
            print(Fore.RED + "Comando inválido, digite \"help\" para ver a lista de comandos\n")

def add_Tarefa(comando):
    task = comando
    task.remove(comando[0])
    execoes = ["add","remove","check","uncheck","exit","done","ls","done","clear","grep","status","edit","exit","help"]

    for i in range(len(task)):
        if task[i] in execoes: 
            print(Fore.RED + f"{task[i]} é um valor invalido.")
        elif task[i] in tarefas:
            print(Fore.RED + f"{task[i]} já existe na lista impossível adicionar.")
        else:   
            tarefa = task[i]
            date = datetime.now().strftime("%Y-%m-%d %H:%M\n")
            tarefas[tarefa] = [date,True, ""]
    adicionar_Tarefa(tarefas)
    exibir_Lista(tarefas, False)

def add_Tarefa_W():
    tarefa = ""

    while tarefa != "done":
        tarefa = input(f"{Style.RESET_ALL}{Back.GREEN}Digite a tarefa:{Style.RESET_ALL} {Fore.GREEN}").lower()
        if tarefa == "done":
            break
        add_Tarefa(["add",tarefa])
        if tarefa in tarefas: 
            desc_ask = input(f"{Style.RESET_ALL}{Back.GREEN}Deseja adicionar alguma descrição na tarefa? Y/N{Style.RESET_ALL} {Fore.GREEN}").lower()
            if desc_ask == 'y':
                desc = input(f"{Style.RESET_ALL}{Back.GREEN}Digite a descrição:{Style.RESET_ALL} {Fore.GREEN}")
                tarefas[tarefa][2] = desc
                adicionar_Tarefa(tarefas)
            else:
                continue

def remove_Tarefa(comando):
    task = comando
    task.remove(comando[0])

    for i in range(len(task)):
        if (task[i]) in tarefas:
            del tarefas[task[i]]
        elif task[i] == "done":
            continue 
        else:
            print(f"{Fore.RED}{task[i]} não está presente na lista de tarefas. Impossível remover. {Style.RESET_ALL}")
    adicionar_Tarefa(tarefas)
    exibir_Lista(tarefas, False)

def remove_Tarefa_W():
    tarefa = ""
    while tarefa != "done":
        tarefa = input(f"{Back.RED} Digite a tarefa que deseja remover:{Style.RESET_ALL} {Fore.RED}").lower()
        remove_Tarefa(["remove",tarefa])

def editar_Tarefa(tarefas,t ):
    exibir_Lista(tarefas, True)

    if t == "Null":
            tarefa = input(f"{Back.GREEN}Digite a tarefa que deseja editar:{Style.RESET_ALL} {Fore.GREEN}").lower()
    else:
        tarefa = t

    if tarefa in tarefas:
        new_Tarefa = input(f"{Back.GREEN}Digite as alterações:{Style.RESET_ALL} {Fore.GREEN}").lower()
        if new_Tarefa != "done":
            date = datetime.now().strftime("%Y-%m-%d %H:%M\n")

            desc_ask = input(f"{Style.RESET_ALL}{Back.GREEN}Deseja adicionar alguma descrição na tarefa? Y/N{Style.RESET_ALL} {Fore.GREEN}").lower()
            if desc_ask == 'y':
                desc = input(f"{Style.RESET_ALL}{Back.GREEN}Digite a descrição:{Style.RESET_ALL} {Fore.GREEN}")
            else:
                desc = ""
            tarefas[new_Tarefa] = [date,True, desc]

            del tarefas[tarefa]
            adicionar_Tarefa(tarefas)
            exibir_Lista(tarefas, False)
    else:
        print(f"{Fore.RED}{tarefa} não está presente na lista de tarefas. Impossível Editar.{Style.RESET_ALL}")

def checked_Tarefa(comando):
    task = comando
    task.remove(comando[0])
    for i in range(len(task)):
        if task[i] in tarefas:
            date = tarefas[task[i]][0]
            tarefas[task[i]] = [date, False]
            adicionar_Tarefa(tarefas)
        else:
            print(f"{Fore.RED}{task[i]} não está presente na lista de tarefas. Impossível marcar como concluido. {Style.RESET_ALL}")
    exibir_Lista(tarefas, False)

def checked_Tarefa_W(comando):
    tarefa = ""
    while tarefa != "done":
        tarefa = input(f"{Style.RESET_ALL}{Back.GREEN}Digite a tarefa que deseja marcar como concluida:{Style.RESET_ALL} {Fore.GREEN}").lower()
        if tarefa == "done":
            break
        checked_Tarefa(["check",tarefa])

def unchecked_Tarefa(comando):
    task = comando
    task.remove(comando[0])
    for i in range(len(task)):
        if task[i] in tarefas:
            date = tarefas[task[i]][0]
            tarefas[task[i]] = [date, True]
            adicionar_Tarefa(tarefas)
        else:
            print(f"{Fore.RED}{task[i]} não está presente na lista de tarefas. Impossível desmarcar como concluido. {Style.RESET_ALL}")
    exibir_Lista(tarefas,False)

def unchecked_Tarefa_W(comando):
    tarefa = ""
    while tarefa != "done":
        tarefa = input(f"{Style.RESET_ALL}{Back.GREEN}Digite a tarefa que deseja desmarcar como concluida:{Style.RESET_ALL} {Fore.GREEN}").lower()
        if tarefa == "done":
            break
        unchecked_Tarefa(["check",tarefa])

def status(x):
    concluidas = 0
    n_concluidas = 0
    for chave, valor in tarefas.items():
        if valor[1]:
            n_concluidas += 1
        elif not valor[1]:
            concluidas += 1
    if not x:
        print(f"{Style.RESET_ALL}{Fore.CYAN}Total de tarefas: {len(tarefas)}\n{Style.RESET_ALL}{Fore.YELLOW}Tarefas concluidas: {concluidas}\n{Style.RESET_ALL}{Fore.MAGENTA}Tarefas não concluidas {n_concluidas}\n")
    elif x:
        concluidas = (concluidas * 100) / len(tarefas)
        n_concluidas = (n_concluidas * 100 / len(tarefas))

        print(f"{Style.RESET_ALL}{Fore.CYAN}Total de tarefas: {len(tarefas)}\n{Style.RESET_ALL}{Fore.YELLOW}Tarefas concluidas: {concluidas}%\n{Style.RESET_ALL}{Fore.MAGENTA}Tarefas não concluidas {n_concluidas}%")

def grep(comando):
    if comando in tarefas:
        if tarefas[comando][1] == True:
            status = "Ativo"
        else:
            status = "Já concluido"
        print(f"{Style.RESET_ALL}{Fore.CYAN}{comando} está presente em sua lista\n{Style.RESET_ALL}{Fore.YELLOW}Data de adição: {tarefas[comando][0].rstrip()}\n{Style.RESET_ALL}{Fore.MAGENTA}Status: {status}\n{Fore.GREEN}Descrição: {tarefas[comando][2]}")

def exibir_Lista(tarefas, x):
    for chave, valor in tarefas.items():
        if valor[1]:
            chave = Style.BRIGHT + Fore.MAGENTA + chave + Style.RESET_ALL
            pontos = Style.BRIGHT + Fore.YELLOW + gerar_Pontos(chave) + Style.RESET_ALL
            data = Style.BRIGHT+ Fore.BLUE + formatar_Data(x, valor[0]) + Style.RESET_ALL
        elif not valor[1]:
            chave = Style.BRIGHT + Fore.BLACK + chave + Style.RESET_ALL
            pontos = Style.BRIGHT + Fore.BLACK + gerar_Pontos(chave) + Style.RESET_ALL
            data = Style.BRIGHT+ Fore.BLACK + formatar_Data(x, valor[0]) + Style.RESET_ALL
        print(f"{chave}{pontos}{data}", end="")
    
def clear_Terminal():
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        subprocess.call('clear', shell=True)
    elif platform.system() == 'Windows':
        subprocess.call('cls', shell=True)

def formatar_Data(x,valor):
    if x:
        return valor[0:16] + "\n"
    else: 
        return valor[0:10] + "\n"

def gerar_Pontos(x):
    y = 40 - len(x)
    pts = ""
    for i in range(y):
        pts +=  "."
    return pts

while(c != "exit"):
    print(f"{Back.GREEN}{Style.BRIGHT}TTLIST: ")
    c = input(Fore.GREEN + ">").lower()
    Style.RESET_ALL
    exec_Comando(c)