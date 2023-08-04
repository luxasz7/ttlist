import json

class Lista_Tarefas:
    def __init__(self):
        with open('arquivo2.json','r') as self.arquivo:
            self.arquivo = json.load(self.arquivo)
        self.tarefas = self.arquivo

    def adicionar(self, tarefas):
        with open('arquivo2.json','w') as self.arquivo:
            json.dump(tarefas, self.arquivo)

    def dic_tarefas(self, tarefas):
        self.tarefas = tarefas
        self.adicionar(tarefas)