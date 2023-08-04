from Lista_Tarefas import Lista_Tarefas
from Tarefa import Tarefa
from Commands import Commands

lista = Lista_Tarefas()
tarefa = Tarefa(lista)
comando = Commands(lista)

comando.ls(False)