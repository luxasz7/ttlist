import colorama
from colorama import init, Fore, Back, Style
colorama.init(autoreset=True)

from Lista_Tarefas import Lista_Tarefas
from Tarefa import Tarefa
from Commands import Commands

lista_tarefas = Lista_Tarefas()

c = ""
tarefas = lista_tarefas.tarefas

tarefa = Tarefa(lista_tarefas)
Commands = Commands(lista_tarefas)

def exec_Comando(c):
    comando = c.split()

    match comando[0]:
        case "add":
            for i in range(1,len(comando)):
                if len(comando[i]) > 35:
                    print(f"{comando[i]} excede o número de caracteres.")
                    comando.remove(comando[i])              
            if len(comando) == 1:
                    tarefa.new_task_w()
            elif len(comando) > 0:
                    tarefa.new_task(comando)
        case "remove":
            if len(comando) == 1:
                tarefa.remove_task_w()
                pass
            else:
                tarefa.remove_task(comando)
        case "check":
                if len(comando) == 1:
                    tarefa.check_task_w()
                elif len(comando) > 0:
                    tarefa.check_task(comando)
        case "uncheck":
            if len(comando) == 1:
                tarefa.uncheck_task_w()
            elif len(comando) > 0:
                tarefa.uncheck_task(comando)
        case "help":
            Commands.help()
        case "exit":
            Commands.exit()
        case "ls":
            if len(comando) == 1:
                Commands.ls(False)
            elif len(comando) == 2 and comando[1] == "-h":
                Commands.ls(True)
            else:
                error()
        case "clear":
            Commands.clear()
        case "edit":
            if len(comando) == 1:
                tarefa.edit_task("Null")
            elif len(comando) == 2:
                tarefa.edit_task(comando[1])
            elif len(comando) > 2:
                error()
        case "status":
            if len(comando) == 1:
                tarefa.status(False)
            elif len(comando) > 1 and comando[1] == 'p':
                tarefa.status(True)
            elif len(comando) > 1 and comando[1] != 'p':
               error()
        case "grep":
            if len(comando) == 2:
                Commands.grep(comando[1])
            elif len(comando) > 2:
                error()
        case other:
            error()
def error():
    print(Fore.RED + "Comando inválido, digite \"help\" para ver a lista de comandos\n")

Commands.clear()

while True:
    print(f"{Back.GREEN}{Style.BRIGHT}{Fore.WHITE}TTLIST: ")
    c = input(Fore.GREEN + ">").lower()

    while c == "":
         c = "."
        
    Style.RESET_ALL   
    exec_Comando(c)
    if c == "exit":
        break