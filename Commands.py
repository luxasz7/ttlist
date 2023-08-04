import colorama
from colorama import init, Fore, Back, Style
import subprocess
import platform


class Commands:
    def __init__(self, Lista_Tarefas):
        self.lista_tarefas = Lista_Tarefas

    def help(self):
        print(f"{Back.LIGHTMAGENTA_EX}--------------------------------------{Style.RESET_ALL}\n{Back.LIGHTBLUE_EX}add - Adiciona uma nova terafa{Style.RESET_ALL}\n{Back.LIGHTBLUE_EX}remove - Remove um tarefa{Style.RESET_ALL}\n{Back.LIGHTBLUE_EX}check - Marca uma tarefa com concluída{Style.RESET_ALL}\n{Back.LIGHTBLUE_EX}ls - Lista as terafas{Style.RESET_ALL}\n{Back.LIGHTBLUE_EX}ls -h - Lista as tarefas exibindo seu horário de criação{Style.RESET_ALL}\n{Back.LIGHTMAGENTA_EX}--------------------------------------{Style.RESET_ALL}")

    def exit(self):
        print(f"{Fore.LIGHTMAGENTA_EX}Saindo")
    
    def ls(self, x):
        #clear_Terminal()
        print(f"{Back.GREEN}{Style.BRIGHT}{Fore.WHITE}TTLIST: ")
        for chave, valor in self.lista_tarefas.tarefas.items():
            if valor[1]:
                chave = Style.BRIGHT + Fore.MAGENTA + chave + Style.RESET_ALL
                pontos = Style.BRIGHT + Fore.YELLOW + self.gerar_Pontos(chave) + Style.RESET_ALL
                data = Style.BRIGHT+ Fore.BLUE + self.formatar_Data(x, valor[0]) + Style.RESET_ALL
            elif not valor[1]:
                chave = Style.BRIGHT + Fore.BLACK + chave + Style.RESET_ALL
                pontos = Style.BRIGHT + Fore.BLACK + self.gerar_Pontos(chave) + Style.RESET_ALL
                data = Style.BRIGHT+ Fore.BLACK + self.formatar_Data(x, valor[0]) + Style.RESET_ALL
            print(f"{chave}{pontos}{data}", end="")

    def formatar_Data(self,x,valor):
        if x:
            return valor[0:16] + "\n"
        else: 
            return valor[0:10] + "\n"

    def gerar_Pontos(self,x):
        y = 40 - len(x)
        pts = ""
        for i in range(y):
            pts +=  "."
        return pts

    def clear(self):
        if platform.system() == 'Linux' or platform.system() == 'Darwin':
            subprocess.call('clear', shell=True)
        elif platform.system() == 'Windows':
            subprocess.call('cls', shell=True)

    def status(self, x):
        #exibir_Lista(tarefas, False)
        print("\n")
        concluidas = 0
        n_concluidas = 0
        for chave, valor in self.lista_tarefas.tarefas.items():
            if valor[1]:
                n_concluidas += 1
            elif not valor[1]:
                concluidas += 1
        if not x:
            print(f"{Style.RESET_ALL}{Fore.CYAN}Total de tarefas: {len(self.lista_tarefas.tarefas)}\n{Style.RESET_ALL}{Fore.YELLOW}Tarefas concluidas: {concluidas}\n{Style.RESET_ALL}{Fore.MAGENTA}Tarefas não concluidas {n_concluidas}\n")
        elif x:
            concluidas = round((concluidas * 100) / len(self.lista_tarefas.tarefas))
            n_concluidas = round((n_concluidas * 100 / len(self.lista_tarefas.tarefas)))

            print(f"{Style.RESET_ALL}{Fore.CYAN}Total de tarefas: {len(self.lista_tarefas)}\n{Style.RESET_ALL}{Fore.YELLOW}Tarefas concluidas: {concluidas}%\n{Style.RESET_ALL}{Fore.MAGENTA}Tarefas não concluidas {n_concluidas}%")

    def grep(self, comando):
        if comando in self.lista_tarefas.tarefas:
            if self.lista_tarefas.tarefas[comando][1] == True:
                status = "Ativo"
            else:
                status = "Já concluido"
            print(f"{Style.RESET_ALL}{Fore.CYAN}{comando} está presente em sua lista\n{Style.RESET_ALL}{Fore.YELLOW}Data de adição: {self.lista_tarefas.tarefas[comando][0].rstrip()}\n{Style.RESET_ALL}{Fore.MAGENTA}Status: {status}\n{Fore.GREEN}Descrição: {self.lista_tarefas.tarefas[comando][2]}")
