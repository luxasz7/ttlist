import colorama
from colorama import init, Fore, Back, Style
colorama.init(autoreset=True)
import pandas as pd

from Lista_Tarefas import Lista_Tarefas
lista_tarefas = Lista_Tarefas()
#df = lista_tarefas.dataframe()

class ls_command:
    def __init__(self, lista_tarefas):
        self.df = lista_tarefas.dataframe()
        
    def ls(self, x):
        def formatar_Data(x, valor):
            if x:
                return valor
            else: 
                return valor.date()

        def gerar_Pontos(x):
            y = 40 - len(x)
            pts = ""
            for i in range(y):
                pts +=  "."
            return pts
        print(f"{Back.GREEN}{Style.BRIGHT}{Fore.WHITE}TTLIST: ")

        for i, j in self.df.iloc[0::, 0:3].iterrows():
            if j[2]:
                j[0] = Style.BRIGHT + Fore.MAGENTA + j[0] + Style.RESET_ALL
                pontos = Style.BRIGHT + Fore.YELLOW + gerar_Pontos(i) + Style.RESET_ALL
                j[1] = Style.BRIGHT+ Fore.BLUE + str(formatar_Data(x, j[1])) + Style.RESET_ALL + "\n"
            elif not j[2]:
                j[0] = Style.BRIGHT + Fore.BLACK + j[0] + Style.RESET_ALL
                pontos = Style.BRIGHT + Fore.BLACK + gerar_Pontos(i) + Style.RESET_ALL
                j[1] = Style.BRIGHT+ Fore.BLACK + str(formatar_Data(x, j[1])) + Style.RESET_ALL + "\n" 
            print(f"{j[0]}{pontos}{j[1]}", end="")


