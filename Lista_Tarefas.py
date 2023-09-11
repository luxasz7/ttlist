import json
import pandas as pd

class Lista_Tarefas:
    def __init__(self):
        with open('arquivo.json','r') as self.arquivo:
            self.arquivo = json.load(self.arquivo)
        self.tarefas = self.arquivo
        self.dataframe()

    def adicionar(self, tarefas):
        with open('arquivo.json','w') as self.arquivo:
            json.dump(tarefas, self.arquivo)

    def dic_tarefas(self, tarefas):
        self.tarefas = tarefas
        self.adicionar(tarefas)
        self.dataframe()

    def dataframe(self):
        if len(self.tarefas) > 0:
            self.df = pd.DataFrame(data = self.tarefas).T
            self.df.columns = ["Name","Datetime","Status","Desc"]
            self.df["Datetime"] = pd.to_datetime(self.df["Datetime"])
            return self.df