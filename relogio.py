import tkinter as tk
import datetime

def hora_atual():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, hora_atual)

# Cria uma janela
window = tk.Tk()
window.title("Relógio Digital")

# Cria um rótulo para exibir a hora
time_label = tk.Label(window, font=("Arial", 80))
time_label.pack(padx=50, pady=50)

# Inicia a atualização da hora
hora_atual()

window.mainloop()