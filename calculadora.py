import tkinter as tk
from tkinter import messagebox

def on_click(botao_texto):
    """Gerencia o que acontece quando um botão é clicado."""
    atual = entrada.get()
    
    if botao_texto == "=":
        try:
            # Avalia a expressão matemática na tela
            resultado = eval(atual)
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, str(resultado))
        except Exception:
            messagebox.showerror("Erro", "Expressão Inválida")
            entrada.delete(0, tk.END)
            
    elif botao_texto == "C":
        entrada.delete(0, tk.END)
        
    else:
        entrada.insert(tk.END, botao_texto)

# Configuração da Janela Principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")

# Campo de exibição (Display)
entrada = tk.Entry(janela, font=("Arial", 24), borderwidth=5, relief="flat", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Definição dos botões
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Criando e posicionando os botões no grid
linha = 1
coluna = 0

for texto in botoes:
    comando = lambda x=texto: on_click(x)
    tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 14),
              command=comando).grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")
    
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# Ajusta o redimensionamento das colunas e linhas
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)
for i in range(1, 5):
    janela.grid_rowconfigure(i, weight=1)

janela.mainloop()