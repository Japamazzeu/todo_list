import tkinter as tk
from tkinter import messagebox

# Funções para manipulação das tarefas
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Você deve inserir uma tarefa.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Aviso", "Você deve selecionar uma tarefa.")

def clear_tasks():
    task_listbox.delete(0, tk.END)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Lista de Tarefas")

# Caixa de entrada para as tarefas
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

# Botões de ação
add_task_button = tk.Button(root, text="Adicionar Tarefa", width=48, command=add_task)
add_task_button.pack(pady=5)

delete_task_button = tk.Button(root, text="Deletar Tarefa", width=48, command=delete_task)
delete_task_button.pack(pady=5)

clear_tasks_button = tk.Button(root, text="Limpar Tarefas", width=48, command=clear_tasks)
clear_tasks_button.pack(pady=5)

# Lista para exibir as tarefas
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Rodar a aplicação
root.mainloop()
