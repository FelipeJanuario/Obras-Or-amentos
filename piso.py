import tkinter as tk
from tkinter import messagebox

def calcular_quantidade_pisos(area_total, area_piso):
    quantidade_pisos = area_total / area_piso
    return quantidade_pisos

def calcular_area_com_excedente(altura, largura, comprimento_piso, largura_piso, excedente_percentual=10):
    # Convertendo a área da parede ou chão para centímetros quadrados
    area_total = (altura * largura) * 10000  # m^2 para cm^2
    # Convertendo a área do piso para centímetros quadrados
    area_piso = comprimento_piso * largura_piso
    
    quantidade_pisos = calcular_quantidade_pisos(area_total, area_piso)
    
    excedente = quantidade_pisos * (excedente_percentual / 100)
    quantidade_total_com_excedente = quantidade_pisos + excedente
    
    return quantidade_total_com_excedente

def calcular():
    try:
        altura = float(entry_altura.get())
        largura = float(entry_largura.get())
        comprimento_piso = float(entry_comprimento_piso.get())
        largura_piso = float(entry_largura_piso.get())
        excedente_percentual = float(entry_excedente.get())
        
        quantidade_pisos = calcular_area_com_excedente(altura, largura, comprimento_piso, largura_piso, excedente_percentual)
        
        messagebox.showinfo("Resultado", f"A quantidade de pisos necessária, incluindo um excedente de {excedente_percentual}%, é: {quantidade_pisos:.2f} pisos.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Configurando a janela principal
root = tk.Tk()
root.title("Calculadora de Pisos")

# Altura da parede ou comprimento do chão
tk.Label(root, text="Altura da parede ou comprimento do chão (m):").grid(row=0, column=0, padx=10, pady=5)
entry_altura = tk.Entry(root)
entry_altura.grid(row=0, column=1, padx=10, pady=5)

# Largura da parede ou do chão
tk.Label(root, text="Largura da parede ou do chão (m):").grid(row=1, column=0, padx=10, pady=5)
entry_largura = tk.Entry(root)
entry_largura.grid(row=1, column=1, padx=10, pady=5)

# Comprimento do piso
tk.Label(root, text="Comprimento do piso (cm):").grid(row=2, column=0, padx=10, pady=5)
entry_comprimento_piso = tk.Entry(root)
entry_comprimento_piso.grid(row=2, column=1, padx=10, pady=5)

# Largura do piso
tk.Label(root, text="Largura do piso (cm):").grid(row=3, column=0, padx=10, pady=5)
entry_largura_piso = tk.Entry(root)
entry_largura_piso.grid(row=3, column=1, padx=10, pady=5)

# Percentual de excedente
tk.Label(root, text="Percentual de excedente (%):").grid(row=4, column=0, padx=10, pady=5)
entry_excedente = tk.Entry(root)
entry_excedente.grid(row=4, column=1, padx=10, pady=5)
entry_excedente.insert(0, "10")  # Valor padrão de 10%

# Botão de cálculo
tk.Button(root, text="Calcular", command=calcular).grid(row=5, columnspan=2, pady=10)

# Executando a aplicação
root.mainloop()
