import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk

def calcular_tijolos():
    try:
        # Leitura das dimensões da parede em metros
        altura_parede = float(entry_altura_parede.get())
        comprimento_parede = float(entry_comprimento_parede.get())
        
        # Leitura das dimensões do tijolo em centímetros e conversão para metros
        altura_tijolo_cm = float(entry_altura_tijolo.get())
        comprimento_tijolo_cm = float(entry_comprimento_tijolo.get())
        espessura_junta_cm = float(entry_espessura_junta.get())
        
        altura_tijolo = altura_tijolo_cm / 100
        comprimento_tijolo = comprimento_tijolo_cm / 100
        espessura_junta = espessura_junta_cm / 100
        
        area_parede = altura_parede * comprimento_parede
        area_tijolo_com_argamassa = (altura_tijolo + espessura_junta) * (comprimento_tijolo + espessura_junta)
        numero_tijolos = area_parede / area_tijolo_com_argamassa
        
        messagebox.showinfo("Resultado", f"Você precisará de aproximadamente {int(numero_tijolos)} tijolos.")
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Configuração da interface gráfica com tema
root = ThemedTk(theme="arc")
root.title("Calculadora de Tijolos")

# Labels e Entries com ttk
ttk.Label(root, text="Altura da Parede (m):").grid(row=0, column=0, padx=10, pady=10)
entry_altura_parede = ttk.Entry(root)
entry_altura_parede.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(root, text="Comprimento da Parede (m):").grid(row=1, column=0, padx=10, pady=10)
entry_comprimento_parede = ttk.Entry(root)
entry_comprimento_parede.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(root, text="Altura do Tijolo (cm):").grid(row=2, column=0, padx=10, pady=10)
entry_altura_tijolo = ttk.Entry(root)
entry_altura_tijolo.grid(row=2, column=1, padx=10, pady=10)

ttk.Label(root, text="Comprimento do Tijolo (cm):").grid(row=3, column=0, padx=10, pady=10)
entry_comprimento_tijolo = ttk.Entry(root)
entry_comprimento_tijolo.grid(row=3, column=1, padx=10, pady=10)

ttk.Label(root, text="Espessura da Junta (cm):").grid(row=4, column=0, padx=10, pady=10)
entry_espessura_junta = ttk.Entry(root)
entry_espessura_junta.grid(row=4, column=1, padx=10, pady=10)

# Botão para calcular
btn_calcular = ttk.Button(root, text="Calcular", command=calcular_tijolos)
btn_calcular.grid(row=5, columnspan=2, pady=20)

root.mainloop()
