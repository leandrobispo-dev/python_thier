import tkinter as tk
from tkinter import messagebox


class BMICalculator:
    def __init__(self):
        # Inicializar a janela principal
        self.root = tk.Tk()
        self.root.title("Calculadora de IMC")

        # Criar os elementos da interface gráfica
        self.create_widgets()

        # Iniciar o loop principal da interface gráfica
        self.root.mainloop()

    def create_widgets(self):
        # Label e Entry para a altura
        self.label_height = tk.Label(self.root, text="Altura (m):")
        self.label_height.grid(row=0, column=0, padx=10, pady=10)
        self.entry_height = tk.Entry(self.root)
        self.entry_height.grid(row=0, column=1, padx=10, pady=10)

        # Label e Entry para o peso
        self.label_weight = tk.Label(self.root, text="Peso (kg):")
        self.label_weight.grid(row=1, column=0, padx=10, pady=10)
        self.entry_weight = tk.Entry(self.root)
        self.entry_weight.grid(row=1, column=1, padx=10, pady=10)

        # Botão para calcular o IMC
        self.button_calculate = tk.Button(self.root, text="Calcular IMC", command=self.calculate_bmi)
        self.button_calculate.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Label para exibir o resultado
        self.label_result = tk.Label(self.root, text="IMC:")
        self.label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def calculate_bmi(self):
        try:
            # Obter altura e peso do usuário
            height = float(self.entry_height.get())
            weight = float(self.entry_weight.get())

            # Calcular o IMC
            bmi = weight / (height ** 2)

            # Exibir o resultado
            self.label_result.config(text=f"IMC: {bmi:.2f}")

            # Mostrar a categoria do IMC
            self.show_bmi_category(bmi)
        except ValueError:
            # Exibir mensagem de erro se a entrada for inválida
            messagebox.showerror("Erro", "Por favor, insira valores válidos para altura e peso.")

    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif 18.5 <= bmi < 24.9:
            category = "Peso normal"
        elif 25 <= bmi < 29.9:
            category = "Sobrepeso"
        else:
            category = "Obesidade"

        # Exibir a categoria do IMC
        messagebox.showinfo("Categoria do IMC", f"Categoria: {category}")


# Executar o programa principal
BMICalculator()
