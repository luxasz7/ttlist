from datetime import datetime
import colorama
from colorama import init, Fore, Back, Style
colorama.init(autoreset=True)
import json
import subprocess
import platform

# arquivo = open('arquivo.txt','r')
# arquivo_Tam = len(arquivo.readlines())
# arquivo.close()

with open('arquivo.json','r') as arquivo:
    arquivo = json.load(arquivo)

c = ""
tarefas = arquivo
#datas = []

# def preencher_Tarefas_Arquivo(x, arquivo_Tam, y):
#     arquivo = open(y,'r')
#     for i in range(arquivo_Tam):
#         valor = arquivo.readline()
#         x.append(valor)
#     arquivo.close()

def adicionar_Tarefa(tarefas):    
    with open('arquivo.json','w') as arquivo:
        json.dump(tarefas, arquivo)

# preencher_Tarefas_Arquivo(tarefas, arquivo_Tam, "arquivo.txt")
# preencher_Tarefas_Arquivo(datas, arquivo_Tam, "data.txt")

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
        case other:
            print(Fore.RED + "Comando inválido, digite \"help\" para ver a lista de comandos\n")
###ADD###
def add_Tarefa(comando):
    task = comando
    task.remove(comando[0])
    
    for i in range(len(task)):
        if task[i] == "add" or task[i] == "remove" or task[i] == "check" or task[i] == "exit" or task[i] == "done" or task[i] == "ls" or task[i] == "done" or task[i] == "clear": 
            print(Fore.RED + f"{task[i]} é um valor invalido.")
        elif task[i] in tarefas:
            print(Fore.RED + f"{task[i]} já existe na lista impossível adicionar.")
        else:   
            tarefa = task[i]
            date = datetime.now().strftime("%Y-%m-%d %H:%M\n")
            tarefas[tarefa] = [date,True]
    adicionar_Tarefa(tarefas)
    exibir_Lista(tarefas, False)

def add_Tarefa_W():
    tarefa = ""

    while tarefa != "done":
        tarefa = input(f"{Back.GREEN}Digite a tarefa:{Style.RESET_ALL} {Fore.GREEN}").lower() #+ "\n"
        add_Tarefa(["add",tarefa])
        # while (tarefa == "add" or tarefa == "remove" or tarefa == "check" or tarefa == "exit" or tarefa == "ls" or tarefa == "clear") or len(tarefa.split()) > 1 or len(tarefa) >= 35:
        #     print(f"{Fore.RED}\n{tarefa.strip()} é um valor invalido. Digite outro nome para a tarefa. {Style.RESET_ALL}\n")
        #     tarefa = input(f"{Back.GREEN}Digite a tarefa:{Style.RESET_ALL} {Fore.GREEN}").lower() #+ "\n"

        # if tarefa in tarefas:
        #     print(f"\n{Fore.RED}{tarefa.strip()} já existe em sua lista. {Style.RESET_ALL}\n")
        # elif tarefa == "done":
        #      break
        # else:
        #     date = datetime.now().strftime("%Y-%m-%d %H:%M\n")
        #     tarefas[tarefa] = date
    #adicionar_Tarefa(tarefas)
    # adicionar_Tarefa(datas, "data.txt")
    #exibir_Lista(tarefas, False)
#######


###REMOVE####
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
    #     if tarefa in tarefas:
    #         del tarefas[tarefa]
    #     elif tarefa == "done":
    #         break
    #     else:
    #         print(f"\n{Fore.RED}{tarefa.strip()} não está em sua lista. Impossível remover.{Style.RESET_ALL}")
    # adicionar_Tarefa(tarefas)
    # exibir_Lista(tarefas, False)
######

def exibir_Lista(tarefas, x):
    for chave, valor in tarefas.items():
        print(f"{Style.BRIGHT + Fore.MAGENTA + chave + Style.RESET_ALL}{Style.BRIGHT + Fore.YELLOW + gerar_Pontos(chave) + Style.RESET_ALL}{Style.BRIGHT+ Fore.BLUE + formatar_Data(x, valor[0]) + Style.RESET_ALL}", end="")

def editar_Tarefa(tarefas,t ):
    exibir_Lista(tarefas, True)

    if t == "Null":
            tarefa = input(f"{Back.GREEN}Digite a tarefa que deseja editar:{Style.RESET_ALL} {Fore.GREEN}").lower()
    else:
        tarefa = t

    if tarefa in tarefas:
        new_Tarefa = input(f"{Back.GREEN}Digite as alterações:{Style.RESET_ALL} {Fore.GREEN}").lower()
        date = datetime.now().strftime("%Y-%m-%d %H:%M\n")
        tarefas[new_Tarefa] = [date,True]

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
        tarefa = input(f"{Back.GREEN}Digite a tarefa que deseja marcar como concluida:{Style.RESET_ALL} {Fore.GREEN}").lower()
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
    exibir_Lista(tarefas,False)

def unchecked_Tarefa_W(comando):
    tarefa = ""
    while tarefa != "done":
        tarefa = input(f"{Back.GREEN}Digite a tarefa que deseja desmarcar como concluida:{Style.RESET_ALL} {Fore.GREEN}").lower()
        if tarefa == "done":
            break
        unchecked_Tarefa(["check",tarefa])

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