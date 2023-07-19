from datetime import datetime
import colorama
from colorama import init, Fore, Back, Style
colorama.init(autoreset=True)

import subprocess
import platform

arquivo = open('arquivo.txt','r')
arquivo_Tam = len(arquivo.readlines())
arquivo.close()

c = ""
tarefas = []
datas = []

def preencher_Tarefas_Arquivo(x, arquivo_Tam, y):
    arquivo = open(y,'r')
    for i in range(arquivo_Tam):
        valor = arquivo.readline()
        x.append(valor)
    arquivo.close()

def adicionar_Tarefa(x, y):
    arquivo = open(y,'w')
    arquivo.write("")
    arquivo.close()

    arquivo = open(y,'a')
    for i in range(len(x)):
        arquivo.write(x[i])
    arquivo.close()

preencher_Tarefas_Arquivo(tarefas, arquivo_Tam, "arquivo.txt")
preencher_Tarefas_Arquivo(datas, arquivo_Tam, "data.txt")

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
                print("check")
        case "help":
            print("-------\nadd - Adiciona uma nova terafa\nremove - Remove um tarefa\ncheck - Marca uma tarefa com concluída\nls - Lista as terafas\n-------")
        case "exit":
            print(f"{Back.LIGHTMAGENTA_EX}Saindo...")
        case "ls":
            if len(comando) == 1:
                exibir_Lista(tarefas,False)
            elif len(comando) == 2 and comando[1] == "-h":
                exibir_Lista(tarefas,True)
            else:
                print(f"{Fore.RED}Comando invalido")
        case "clear":
            clear_Terminal()
        case other:
            print(Fore.RED + "\nComando inválido, digite \"help\" para ver a lista de comandos\n")
###ADD###
def add_Tarefa(comando):
    task = comando
    task.remove(comando[0])
    
    for i in range(len(task)):
        if task[i] == "add" or task[i] == "remove" or task[i] == "check" or task[i] == "exit" or task[i] == "done" or task[i] == "ls" or task[i] == "done" or task[i] == "clear": 
            print(Fore.RED + f"{task[i]} é um valor invalido.")
        elif task[i]+"\n" in tarefas:
            print(Fore.RED + f"{task[i]} já existe na lista impossível adicionar.")
        else:   
            tarefas.append(task[i]+"\n")
            date = datetime.now()
            datas.append(date.strftime("%Y-%m-%d %H:%M\n"))
    adicionar_Tarefa(tarefas, "arquivo.txt")
    adicionar_Tarefa(datas, "data.txt")
    exibir_Lista(tarefas, False)

def add_Tarefa_W():
    tarefa = ""

    while tarefa != "done\n":
        tarefa = input(f"{Back.GREEN}Digite a tarefa:{Style.RESET_ALL} {Fore.GREEN}").lower() + "\n"

        while (tarefa == "add\n" or tarefa == "remove\n" or tarefa == "check\n" or tarefa == "exit\n" or tarefa == "ls\n" or tarefa == "clear\n") or len(tarefa.split()) > 1 or len(tarefa) >= 35:
            print(f"{Fore.RED}\n{tarefa.strip()} é um valor invalido. Digite outro nome para a tarefa. {Style.RESET_ALL}\n")
            tarefa = input(f"{Back.GREEN}Digite a tarefa:{Style.RESET_ALL} {Fore.GREEN}").lower() + "\n"

        if tarefa in tarefas:
            print(f"\n{Fore.RED}{tarefa.strip()} já existe em sua lista. {Style.RESET_ALL}\n")
        elif tarefa == "done\n":
             break
        else:
            tarefas.append(tarefa)
            date = datetime.now()
            datas.append(date.strftime("%Y-%m-%d %H:%M\n"))
    adicionar_Tarefa(tarefas, "arquivo.txt")
    adicionar_Tarefa(datas, "data.txt")
    exibir_Lista(tarefas, False)
#######


###REMOVE####
def remove_Tarefa(comando):
    task = comando
    task.remove(comando[0])

    for i in range(len(task)):
        if (task[i]+"\n") in tarefas:
            tarefas.remove(task[i]+"\n")
            datas.remove(datas[i])
        else:
            print(f"{Fore.RED}{task[i]} não está presente na lista de tarefas. Impossível remover. {Style.RESET_ALL}")
    adicionar_Tarefa(tarefas, "arquivo.txt")
    adicionar_Tarefa(datas, "data.txt")
    exibir_Lista(tarefas, False)

def remove_Tarefa_W():
    tarefa = ""
    while tarefa != "done\n":
        tarefa = input(f"{Back.RED} Digite a tarefa que deseja remover:{Style.RESET_ALL} {Fore.RED}").lower() + "\n"
        if tarefa in tarefas:
            date = datas[tarefas.index(tarefa)]
            tarefas.remove(tarefa)
            datas.remove(date)
        elif tarefa == "done\n":
            break
        else:
            print(f"\n{Fore.RED}{tarefa.strip()} não está em sua lista. Impossível remover.{Style.RESET_ALL}")
    adicionar_Tarefa(tarefas, "arquivo.txt")
    adicionar_Tarefa(datas, "data.txt")
    exibir_Lista(tarefas, False)
######

def exibir_Lista(tarefas, x):
    print("\n")
    for i in range(len(tarefas)):
        print(f"{Style.BRIGHT + Fore.MAGENTA + tarefas[i].strip() + Style.RESET_ALL}{Style.BRIGHT + Fore.YELLOW + gerar_Pontos(tarefas[i]) + Style.RESET_ALL}{Style.BRIGHT+ Fore.BLUE + formatar_Data(x,i) + Style.RESET_ALL}", end ="")
    print("\n")

def clear_Terminal():
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        subprocess.call('clear', shell=True)
    elif platform.system() == 'Windows':
        subprocess.call('cls', shell=True)

def formatar_Data(x,i):
    if x:
        return datas[i][0:16] + "\n"
    else: 
        return datas[i][0:10] + "\n"

def gerar_Pontos(x):
    y = 40 - len(x)
    pts = ""
    for i in range(y):
        pts +=  "."
    return pts

while(c != "exit"):
    print(f"{Back.GREEN}{Style.BRIGHT}TTLIST: ")
    c = input(Fore.GREEN + ">").lower()
    print(Style.RESET_ALL)
    exec_Comando(c)