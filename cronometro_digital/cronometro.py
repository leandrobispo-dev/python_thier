import tkinter as tk


class Stopwatch:
    def __init__(self):
        # Inicializar a janela principal
        self.root = tk.Tk()
        self.root.title("Cronômetro")

        # Inicializar o cronômetro com horas, minutos e segundos configurados para zero
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.running = False

        # Criar os elementos da interface gráfica
        self.create_widgets()

        # Iniciar o loop principal da interface gráfica
        self.root.mainloop()

    def create_widgets(self):
        # Label para mostrar o tempo do cronômetro
        self.label_time = tk.Label(self.root, text="00:00:00", font=("Helvetica", 48))
        self.label_time.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Botão para iniciar o cronômetro
        self.button_start = tk.Button(self.root, text="Iniciar", command=self.start)
        self.button_start.grid(row=1, column=0, padx=10, pady=10)

        # Botão para parar o cronômetro
        self.button_stop = tk.Button(self.root, text="Parar", command=self.stop)
        self.button_stop.grid(row=1, column=1, padx=10, pady=10)

        # Botão para resetar o cronômetro
        self.button_reset = tk.Button(self.root, text="Resetar", command=self.reset)
        self.button_reset.grid(row=1, column=2, padx=10, pady=10)

    def update_time(self):
        if self.running:
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1

            # Atualizar o display do cronômetro
            self.label_time.config(text=f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}")

            # Chamar a função update_time novamente após 1 segundo
            self.root.after(1000, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def stop(self):
        self.running = False

    def reset(self):
        if not self.running:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
            self.label_time.config(text="00:00:00")


# Executar o programa principal
Stopwatch()
