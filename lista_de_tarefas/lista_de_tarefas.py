import tkinter as tk
from tkinter import messagebox


class ToDoListApp:
    def __init__(self):
        # Inicializar a janela principal
        self.root = tk.Tk()
        self.root.title("Lista de Tarefas")

        # Criar a lista de tarefas
        self.tasks = []

        # Criar os elementos da interface gráfica
        self.create_widgets()

        # Iniciar o loop principal da interface gráfica
        self.root.mainloop()

    def create_widgets(self):
        # Entry para a nova tarefa
        self.entry_task = tk.Entry(self.root, width=40)
        self.entry_task.grid(row=0, column=0, padx=10, pady=10)

        # Botão para adicionar tarefa
        self.button_add = tk.Button(self.root, text="Adicionar Tarefa", command=self.add_task)
        self.button_add.grid(row=0, column=1, padx=10, pady=10)

        # Listbox para exibir as tarefas
        self.listbox_tasks = tk.Listbox(self.root, width=50, height=15)
        self.listbox_tasks.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Botão para remover tarefa
        self.button_remove = tk.Button(self.root, text="Remover Tarefa", command=self.remove_task)
        self.button_remove.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.entry_task.delete(0, tk.END)
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Aviso", "A tarefa não pode estar vazia.")

    def remove_task(self):
        try:
            selected_task_index = self.listbox_tasks.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Aviso", "Nenhuma tarefa selecionada.")

    def update_tasks_listbox(self):
        # Limpar a listbox
        self.listbox_tasks.delete(0, tk.END)
        # Adicionar as tarefas atualizadas
        for task in self.tasks:
            self.listbox_tasks.insert(tk.END, task)


# Executar o programa principal
ToDoListApp()
