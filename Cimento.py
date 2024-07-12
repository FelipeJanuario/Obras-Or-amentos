import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk

def calcular_cimento():
    try:
        # Informações para o cálculo do concreto
        comprimento_fundacao = float(entry_comprimento_fundacao.get())
        largura_fundacao = float(entry_largura_fundacao.get())
        profundidade_fundacao = float(entry_profundidade_fundacao.get())
        
        numero_pilares = int(entry_numero_pilares.get())
        altura_pilar = float(entry_altura_pilar.get())
        largura_pilar = float(entry_largura_pilar.get())
        profundidade_pilar = float(entry_profundidade_pilar.get())
        
        area_laje = float(entry_area_laje.get())
        espessura_laje = float(entry_espessura_laje.get())
        
        # Informações para o cálculo da argamassa
        area_paredes = float(entry_area_paredes.get())
        espessura_revestimento = float(entry_espessura_revestimento.get())
        
        # Calcular volumes
        volume_fundacao = comprimento_fundacao * largura_fundacao * profundidade_fundacao
        volume_pilares = numero_pilares * altura_pilar * largura_pilar * profundidade_pilar
        volume_laje = area_laje * espessura_laje
        
        volume_concreto = volume_fundacao + volume_pilares + volume_laje
        volume_argamassa = area_paredes * espessura_revestimento
        
        # Calcular quantidade de cimento
        cimento_concreto = volume_concreto * (1 / 6) * 1440
        cimento_argamassa = volume_argamassa * (1 / 4) * 1440
        
        total_cimento = cimento_concreto + cimento_argamassa
        sacos_cimento = total_cimento / 50
        
        # Exibir resultados
        messagebox.showinfo("Resultados",
                            f"Volume total de concreto necessário: {volume_concreto:.2f} m³\n"
                            f"Volume total de argamassa necessário: {volume_argamassa:.2f} m³\n"
                            f"Quantidade total de cimento necessário: {total_cimento:.2f} kg\n"
                            f"Total de sacos de cimento (50 kg): {sacos_cimento:.2f} sacos")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Criar a janela principal
root = ThemedTk(theme="breeze")
root.title("Calculadora de Cimento")

# Criar e posicionar os widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Comprimento da fundação (m):").grid(row=0, column=0, sticky=tk.W)
entry_comprimento_fundacao = ttk.Entry(frame)
entry_comprimento_fundacao.grid(row=0, column=1)

ttk.Label(frame, text="Largura da fundação (m):").grid(row=1, column=0, sticky=tk.W)
entry_largura_fundacao = ttk.Entry(frame)
entry_largura_fundacao.grid(row=1, column=1)

ttk.Label(frame, text="Profundidade da fundação (m):").grid(row=2, column=0, sticky=tk.W)
entry_profundidade_fundacao = ttk.Entry(frame)
entry_profundidade_fundacao.grid(row=2, column=1)

ttk.Label(frame, text="Número de pilares:").grid(row=3, column=0, sticky=tk.W)
entry_numero_pilares = ttk.Entry(frame)
entry_numero_pilares.grid(row=3, column=1)

ttk.Label(frame, text="Altura de cada pilar (m):").grid(row=4, column=0, sticky=tk.W)
entry_altura_pilar = ttk.Entry(frame)
entry_altura_pilar.grid(row=4, column=1)

ttk.Label(frame, text="Largura de cada pilar (m):").grid(row=5, column=0, sticky=tk.W)
entry_largura_pilar = ttk.Entry(frame)
entry_largura_pilar.grid(row=5, column=1)

ttk.Label(frame, text="Profundidade de cada pilar (m):").grid(row=6, column=0, sticky=tk.W)
entry_profundidade_pilar = ttk.Entry(frame)
entry_profundidade_pilar.grid(row=6, column=1)

ttk.Label(frame, text="Área da laje (m²):").grid(row=7, column=0, sticky=tk.W)
entry_area_laje = ttk.Entry(frame)
entry_area_laje.grid(row=7, column=1)

ttk.Label(frame, text="Espessura da laje (m):").grid(row=8, column=0, sticky=tk.W)
entry_espessura_laje = ttk.Entry(frame)
entry_espessura_laje.grid(row=8, column=1)

ttk.Label(frame, text="Área total das paredes (m²):").grid(row=9, column=0, sticky=tk.W)
entry_area_paredes = ttk.Entry(frame)
entry_area_paredes.grid(row=9, column=1)

ttk.Label(frame, text="Espessura do revestimento (m):").grid(row=10, column=0, sticky=tk.W)
entry_espessura_revestimento = ttk.Entry(frame)
entry_espessura_revestimento.grid(row=10, column=1)

ttk.Button(frame, text="Calcular", command=calcular_cimento).grid(row=11, column=0, columnspan=2)

# Configurar redimensionamento
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
